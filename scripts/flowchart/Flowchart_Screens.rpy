# ------------------------------------------------------------------------ Flowchart Screens
screen key_listener():
    
    key "K_a" action ShowMenu("act_selection")
    python:
        print("Key 'A' pressed, showing act selection screen.")
    key "K_f" action ShowMenu("detroit_flowchart")
    python:
        print("Key 'F' pressed, showing flowchart screen.")
    key "K_d" action ShowMenu("debug_flowchart")
    python:
        print("Key 'D' pressed, showing debug flowchart screen.")
    key "K_i" action ShowMenu("immersion_summary")
    python:
        print("Key 'I' pressed, showing immersion tracker screen and emotional profile.")


screen progress_tooltip(value):
    zorder 100
    frame:
        xalign 0.5
        ypos 100
        background "#3a7bbd"
        padding (10, 5)
        text "Completion: {}%".format(value):
            style "flowchart_tooltip_text"

            font "gui/fonts/Rajdhani-SemiBold.ttf"    
            size 16
            color "#FFFFFF"
screen detroit_flowchart_button():
    zorder 100
    vbox:
        align (0.98, 0.10)
        
        textbutton "FLOWCHART":
            action ShowMenu("detroit_flowchart")
            text_size 20
            text_color "#FFFFFF"
            background "#0066CC"
            hover_background "#4285F4"
            padding (20, 10)
default drawn_connections = set()

screen detroit_flowchart(act_title=None, custom_path=None):
    tag menu

    # Dynamically fetch the flowchart from the manager
    default current_arc = flowchart_manager.get_current_arc()
    default fc = current_arc.flowchart if current_arc else None
    default act_title = act_title or (current_arc.title if current_arc else "Story Flowchart")
    default progression_path = custom_path or (fc.get_flattened_path() if fc else [])
    default progression = calculate_dynamic_progression(fc, progression_path) if fc else 0
    python:
        drawn_connections = set()
    add "flowchart_video"


    # Title bar section
    frame:
        xfill True
        ysize 200
        ypos 70
        background None

        vbox:
            spacing 20
            xpos 60
            ypos 70

            text "{:.0f}% COMPLETED".format(fc.calculate_completion() if fc else 0):
                size 18
                color "#444444"

            frame:
                xsize 1200
                ysize 2
                background "#444444"

            # text act_title:
            #     size 42
            #     color "#444444"

    # Flowchart display
    viewport:
        id "flowchart_viewport"
        xfill True
        yfill True
        ypos 220
        xsize 2520
        ysize 900
        draggable True
        mousewheel True
        child_size (5000, 900)

            
        for node in fc.nodes.values():
            for conn in node.connections:
                $ target_id = conn.get("target", None)
                $ connection_type = conn.get("type", "normal")

                if not target_id or target_id not in fc.nodes:
                    $ print(f"Skipping invalid connection: {node.id} -> {target_id}")
                    continue

                $ pair = (node.id, target_id)
                if pair not in drawn_connections:
                    $ drawn_connections.add(pair)
                    $ conn_node = fc.nodes[target_id]
                    $ is_visited = pair in fc.visited_paths
                    
                    # Add debugging here
                    $ print(f"Drawing connection: {node.id} -> {target_id}")
                    
                    # Rest of drawing code...

                    add DynamicDisplayable(
                        draw_detroit_connection,
                        node,
                        conn_node,
                        fc.nodes.values(),
                        color="#3a7bbd" if is_visited else "#5a5a5a",
                        width=3 if is_visited else 2,
                        connection_type=connection_type,
                        is_visited=is_visited
                    )

        for node_id, node in fc.nodes.items():
            $ style = get_node_style(node, fc.current_node)

            frame:
                background style["bg_color"]
                xpos int(node.x * fc.zoom_level)
                ypos int(node.y * fc.zoom_level)
                xsize style["width"]
                ysize style["height"]

                if node.visited:
                    add Solid("#ffffff55"):
                        xsize style["width"]
                        ysize style["height"]

                button:
                    xfill True
                    yfill True
                    action If(node.visited, Jump(node.label), NullAction())

                    if node.major_event:
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 5
                            text node.title:
                                size 18
                                color style["text_color"]
                                xalign 0.5
                                font "gui/fonts/Rajdhani-SemiBold.ttf"

                            if node.subtitle:
                                text node.subtitle:
                                    size 14
                                    color "#aaaaaa"
                                    xalign 0.5
                                    font "gui/fonts/Rajdhani-Medium.ttf"
                    else:
                        hbox:
                            spacing 10
                            xalign 0.5
                            yalign 0.5
                            text node.title:
                                size 16
                                color style["text_color"]
                                xalign 0.5
                                font "gui/fonts/Rajdhani-Medium.ttf"

                            if node.completion_rate is not None:
                                text "[node.completion_rate]%":
                                    size 16
                                    color "#ffffff"
                                    xalign 1.0

            # Border highlights
            add Solid(style["border_color"], xsize=style["width"], ysize=2, xpos=node.x, ypos=node.y)
            add Solid(style["border_color"], xsize=style["width"], ysize=2, xpos=node.x, ypos=node.y + style["height"] - 2)
            add Solid(style["border_color"], xsize=2, ysize=style["height"], xpos=node.x, ypos=node.y)
            add Solid(style["border_color"], xsize=2, ysize=style["height"], xpos=node.x + style["width"] - 2, ypos=node.y)

            if node.major_event and node.visited and hasattr(node, 'thumbnail') and node.thumbnail:
                frame:
                    xpos node.x - 100
                    ypos node.y - 10
                    xsize 90
                    ysize 80

                    add node.thumbnail:
                        size (90, 80)

                    if node.id == fc.current_node:
                        add Solid("#3a7bbd", xsize=90, ysize=3, xpos=0, ypos=0)
                        add Solid("#3a7bbd", xsize=90, ysize=3, xpos=0, ypos=77)
                        add Solid("#3a7bbd", xsize=3, ysize=80, xpos=0, ypos=0)
                        add Solid("#3a7bbd", xsize=3, ysize=80, xpos=87, ypos=0)

    # Bottom Buttons
    frame:
        xfill True
        yalign 0.97
        background None

        hbox:
            xalign 0.5
            spacing 40

            for button_text, button_action in [
                ("ZOOM IN", Function(fc.zoom_in)),
                ("ZOOM OUT", Function(fc.zoom_out)),
                ("RESET VIEW", SetField(fc, "view_center", (500, 500))),
                ("BACK", Return())
            ]:
                textbutton button_text:
                    action button_action
                    text_size 20
                    text_color "#FFFFFF"
                    background "#0066CC"
                    hover_background "#4285F4"
                    padding (20, 10)

    python:
        print(f"Drawing {len(fc.nodes)} nodes and {len(drawn_connections)} connections")


default selected_arc_id = None

    # timer 2 action Function(debug_check_flowchart, fc)
screen act_selection():
    tag menu

    use game_menu(_("Act Selection"), scroll="viewport"):

        frame:
            xalign 0.5
            yalign 0.5
            background None
            has vbox:
                align (0.5, 0.5)
                spacing 30


            parallax_viewport:
                id "act_scroll"
                xysize (1480, 300)
                draggable True
                mousewheel "horizontal"
                edgescroll (100, 300)

                has fixed style "vparallax_fixed"

                # Horizontal scroll layer
                fixed:
                    fit_first True
                    hbox:
                        spacing 80
                        for arc_id, arc in flowchart_manager.arcs.items():
                            if arc.unlocked:
                                button:
                                    xsize 400
                                    ysize 225
                                    action SetScreenVariable("selected_arc_id", arc_id)


                                    add arc.thumbnail zoom 0.2

                                    frame:
                                        background None
                                        yoffset 220
                                        xfill True
                                        yfill False

                                        vbox:
                                            spacing 4
                                            xalign 0.5
                                            text arc.title:
                                                style "flowchart_node_text"
                                                xalign 0.5
                                                color "#404040"
                                            text arc.description:
                                                size 14
                                                xalign 0.5
                                                color "#151212"
                            else:
                                frame:
                                    background "#333333"
                                    xsize 400
                                    ysize 225
                                    text "LOCKED":
                                        style "flowchart_node_text"
                                        xalign 0.5
                                        yalign 0.5

    if selected_arc_id:
        $ selected_arc = flowchart_manager.arcs[selected_arc_id]
        frame:
            style "menu_frame"
            at truecenter
            padding (40, 30)
            xsize 700
            background "#000000DD"

            vbox:
                spacing 25
                xalign 0.5

                text "What would you like to do with '{}'?".format(selected_arc.title):
                    style "menu_text"
                    xalign 0.5

                hbox:
                    spacing 40
                    xalign 0.5

                    textbutton "Start Act":
                        action [
                            SetField(flowchart_manager, "current_arc", selected_arc_id),
                            Jump(selected_arc.start_label)
                        ]
                        xminimum 220

                    textbutton "View Flowchart":
                        action [
                            Function(flowchart_manager.current_arc, selected_arc_id),
                            Show("detroit_flowchart")
                        ]
                        xminimum 220

                textbutton "Cancel":
                    action SetScreenVariable("selected_arc_id", None)
                    xalign 0.5

screen debug_flowchart():
    zorder 1000
    frame:
        xalign 0.95 ypos 50
        vbox:
            text "Current Arc: [flowchart_manager.current_arc]"
            text "Global Completion: [flowchart_manager.global_completion:.1f]%"
            for arc_id, arc in flowchart_manager.arcs.items():
                textbutton "[arc_id] ({arc.completion:.1f}%)":
                    action [SetField(flowchart_manager, "current_arc", arc_id),
                            Show("detroit_flowchart")]
# ------------------------------------------------------------------------ Flowchart Styles

style flowchart_header:
    font "gui/fonts/Rajdhani-Bold.ttf"
    size 28
    color "#ffffff"
style flowchart_subheader:
    font "gui/fonts/Rajdhani-Medium.ttf"
    size 18
    color "#aaaaaa"
style detroit_button:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 16
    color "#ffffff"
    background "#333333"
    hover_background "#3a7bbd"
    padding (15, 10)
    xsize 180
style detroit_bottom_button:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 18
    color "#ffffff"
    background "#333333"
    hover_background "#3a7bbd"
    padding (15, 10)
style flowchart_progress_text:
    font "gui/fonts/Rajdhani-SemiBold.ttf"
    size 18
    color "#AAAAAA"
style flowchart_act_header:
    font "gui/fonts/Rajdhani-SemiBold.ttf"    
    size 42
    color "#FFFFFF"