init -999 python:
    def init_act1_flowchart():
        flowchart = Flowchart("AI Academy Story")

        # ===== POSITION CONSTANTS =====
        COLUMN_SPACING = 300
        ROW_SPACING = 150
        BRANCH_OFFSET = 200

        # ===== ACT 1: CORE PATH =====
        core_nodes = [
            FlowchartNode(id="start", title="STORY BEGINNING", label="start", 
                        x=200, y=300, major=True, subtitle="CHECKPOINT"),

            FlowchartNode(id="wakeup_intro", title="MORNING ROUTINE", label="wakeup_intro", 
                        x=550, y=350),

            FlowchartNode(id="journey_to_classroom", title="ARRIVAL AT SCHOOL", label="journey_to_classroom", 
                        x=850, y=300, major=True),

            FlowchartNode(id="scene2b", title="DETERMINISTIC SYSTEMS", label="scene2b", 
                        x=1500, y=300, major=True, completion_rate=30),

            FlowchartNode(id="scene2b5_transition", title="POST-CLASS CHOICE", label="scene2b5_transition", 
                        x=1900, y=300, major=True),

            FlowchartNode(id="mai_walk_choice", title="WALK WITH MAI", label="mai_walk_choice", 
                        x=2200, y=150),

            FlowchartNode(id="courtyard_enter_option", title="ENTER WITH JENNIE", label="courtyard_enter_option", 
                        x=1200, y=150),

            FlowchartNode(id="courtyard_separate_option", title="ENTER ALONE", label="courtyard_separate_option", 
                        x=1200, y=450)
        ]

        branch_nodes = [
            FlowchartNode(id="walk_alone", title="WALK ALONE", label="walk_alone_after_class", 
                        x=2200, y=450),

            FlowchartNode(id="forest_path", title="FOREST PATH", label="forest_path_cutscene", 
                        x=2400, y=150, major=True),

            FlowchartNode(id="forest_success", title="QUIZ SUCCESS", label="forest_path_quiz_outro", 
                        x=2900, y=50),

            FlowchartNode(id="forest_partial", title="QUIZ PARTIAL", label="forest_path_quiz_outro", 
                        x=2900, y=150),

            FlowchartNode(id="forest_fail", title="QUIZ FAIL", label="forest_path_quiz_outro", 
                    x=2900, y=250),

            FlowchartNode(id="jennie_friend_accept", title="FRIENDSHIP ACCEPTED", label="forest_path_friend_accept", 
                        x=3200, y=0, node_type="outcome"),

            FlowchartNode(id="jennie_friend_decline", title="FRIENDSHIP DECLINED", label="forest_path_friend_decline", 
                        x=3200, y=100, node_type="outcome")
        ]

        for node in core_nodes + branch_nodes:
            flowchart.add_node(node)

        # ===== CONNECTIONS =====
        flowchart.nodes["start"].add_connection("wakeup_intro", connection_type="linear", choice_data={
            "impact_type": "knowledge", "magnitude": 1, "feedback_text": "Begins your first day at AI Academy"
        })

        flowchart.nodes["wakeup_intro"].add_connection("journey_to_classroom", connection_type="linear", choice_data={
            "impact_type": "knowledge", "magnitude": 1, "feedback_text": "You prepare for school"
        })

        # flowchart.nodes["journey_to_classroom"].add_connection("scene2b", connection_type="linear", choice_data={
        #     "impact_type": "knowledge", "magnitude": 2, "feedback_text": "Start learning about deterministic systems"
        # })

        flowchart.nodes["scene2b"].add_connection("scene2b5_transition", connection_type="linear", choice_data={
            "impact_type": "learning", "magnitude": 2, "feedback_text": "Class ends, choices open"
        })

        flowchart.nodes["scene2b5_transition"].add_connection("walk_alone", connection_type="choice", choice_data={
            "impact_type": "reflection", "magnitude": 1, "feedback_text": "Walk alone to reflect"
        })

        flowchart.nodes["scene2b5_transition"].add_connection("mai_walk_choice", connection_type="choice", choice_data={
            "impact_type": "relationships", "magnitude": 1, "feedback_text": "Walk with Mai to deepen your bond"
        })

        flowchart.nodes["mai_walk_choice"].add_connection("forest_path", connection_type="linear", choice_data={
            "impact_type": "glitches", "magnitude": 1, "feedback_text": "Take the forest path — something shifts"
        })

        flowchart.nodes["walk_alone"].add_connection("after_school_walk", connection_type="linear", choice_data={
            "impact_type": "reflection", "magnitude": 0.5, "feedback_text": "Your solo walk increases insight"
        })

        flowchart.nodes["forest_path"].add_connection("forest_success", connection_type="quiz", choice_data={
            "impact_type": "knowledge", "magnitude": 2, "feedback_text": "Perfect quiz answers"
        })

        flowchart.nodes["forest_path"].add_connection("forest_partial", connection_type="quiz", choice_data={
            "impact_type": "knowledge", "magnitude": 1, "feedback_text": "Partially correct answers"
        })

        flowchart.nodes["forest_path"].add_connection("forest_fail", connection_type="quiz", choice_data={
            "impact_type": "glitches", "magnitude": 1, "feedback_text": "Quiz failed, relationship hurt"
        })

        flowchart.nodes["forest_success"].add_connection("jennie_friend_accept", connection_type="branch", choice_data={
            "impact_type": "relationships", "magnitude": 2, "feedback_text": "You accepted Jennie's friendship"
        })

        flowchart.nodes["forest_success"].add_connection("jennie_friend_decline", connection_type="branch", choice_data={
            "impact_type": "reflection", "magnitude": 1, "feedback_text": "You declined Jennie's friendship"
        })

        flowchart.nodes["journey_to_classroom"].add_connection("courtyard_enter_option", connection_type="choice", choice_data={
            "impact_type": "relationships", "magnitude": 0.5, "feedback_text": "Entered school with Jennie"
        })

        flowchart.nodes["journey_to_classroom"].add_connection("courtyard_separate_option", connection_type="choice", choice_data={
            "impact_type": "relationships", "magnitude": -0.5, "feedback_text": "Chose to enter alone"
        })

        flowchart.nodes["courtyard_separate_option"].add_connection("scene2b", connection_type="choice", choice_data={
            "impact_type": "relationships", "magnitude": -0.5, "feedback_text": "Chose to enter alone"
        })

        flowchart.nodes["courtyard_enter_option"].add_connection("scene2b", connection_type="choice", choice_data={
            "impact_type": "relationships", "magnitude": -0.5, "feedback_text": "Chose to enter alone"
        })

        return flowchart


    def init_act2_flowchart():
        flowchart = Flowchart("Act 2: Determination")

        # Position constants
        COLUMN_SPACING = 300
        ROW_SPACING = 150
        BRANCH_OFFSET = 200

        # Core nodes
        core_nodes = [
            FlowchartNode(id="scene2d", title="DETERMINISTIC SYSTEMS", label="scene2d",
                        x=200, y=300, major=True, completion_rate=15),
            
            FlowchartNode(id="deterministic_choice", title="SYSTEMS REFLECTION", label="deterministic_post_choice",
                        x=500, y=300),
            
            FlowchartNode(id="neuralnet_intro", title="NEURAL NET BASICS", label="neuron_activation_post_choice",
                        x=800, y=300, major=True),
            
            FlowchartNode(id="backprop_lesson", title="BACKPROPAGATION", label="backprop_post_choice",
                        x=1100, y=300),
            
            FlowchartNode(id="classifier_lesson", title="DECISION TREES", label="classifier_teaching",
                        x=1400, y=300, major=True, completion_rate=30),
            
            FlowchartNode(id="scene2d_transition", title="FRIENDSHIP CRISIS", label="scene2d_transition",
                        x=1700, y=300, major=True),
            
            FlowchartNode(id="help_mai", title="HELP MAI", label="help_mai",
                        x=2000, y=150),
            
            FlowchartNode(id="help_eren", title="HELP EREN", label="help_eren",
                        x=2000, y=450)
        ]

        # Branch nodes
        branch_nodes = [
            FlowchartNode(id="sketchbook_found", title="SKETCHBOOK RECOVERED", label="mai_search_success",
                        x=2300, y=150, node_type="outcome"),
            
            FlowchartNode(id="sketchbook_lost", title="SKETCHBOOK LOST", label="mai_search_fail",
                        x=2300, y=250),
            
            FlowchartNode(id="kuma_found", title="CAT AND BROTHER FOUND", label="eren_search_success",
                        x=2300, y=450, node_type="outcome"),
            
            FlowchartNode(id="kuma_lost", title="SEARCH FAILED", label="eren_search_fail",
                        x=2300, y=550)
        ]

        # Add all nodes
        for node in core_nodes + branch_nodes:
            flowchart.add_node(node)

        # Connections
        connections = [
            ("scene2d", "deterministic_choice", "linear", {"impact_type": "knowledge", "magnitude": 1, "feedback_text": "Introduction to deterministic systems"}),
            
            ("deterministic_choice", "neuralnet_intro", "linear",
            {"impact_type": "learning", "magnitude": 1, "feedback_text": "Transition to neural networks"}),
            
            ("neuralnet_intro", "backprop_lesson", "linear",
            {"impact_type": "knowledge", "magnitude": 2, "feedback_text": "Learning backpropagation"}),
            
            ("backprop_lesson", "classifier_lesson", "linear",
            {"impact_type": "learning", "magnitude": 2, "feedback_text": "Decision trees explained"}),
            
            ("classifier_lesson", "scene2d_transition", "linear",
            {"impact_type": "relationships", "magnitude": 1, "feedback_text": "Class ends, crisis begins"}),
            
            ("scene2d_transition", "help_mai", "choice",
            {"impact_type": "relationships", "magnitude": 2, "feedback_text": "Choose to help Mai"}),
            
            ("scene2d_transition", "help_eren", "choice",
            {"impact_type": "relationships", "magnitude": 2, "feedback_text": "Choose to help Eren"}),
            
            ("help_mai", "sketchbook_found", "quiz",
            {"impact_type": "relationships", "magnitude": 3, "feedback_text": "Successfully found sketchbook"}),
            
            ("help_mai", "sketchbook_lost", "quiz",
            {"impact_type": "glitches", "magnitude": 1, "feedback_text": "Failed to find sketchbook"}),
            
            ("help_eren", "kuma_found", "quiz",
            {"impact_type": "relationships", "magnitude": 3, "feedback_text": "Found Eren's brother and cat"}),
            
            ("help_eren", "kuma_lost", "quiz",
            {"impact_type": "glitches", "magnitude": 1, "feedback_text": "Failed to find them"})
        ]

        for src, dest, conn_type, data in connections:
            flowchart.nodes[src].add_connection(dest, connection_type=conn_type, choice_data=data)

        return flowchart
    def init_act3_flowchart():
        flowchart = Flowchart("Act 3: Isolation")

        # Position constants
        COLUMN_SPACING = 300
        ROW_SPACING = 150
        BRANCH_OFFSET = 200

        # Core nodes
        core_nodes = [
            FlowchartNode(id="scene3_1_5", title="EMPTY HALLWAYS", label="scene3_1_5", 
                        x=200, y=300, major=True, completion_rate=10),
            
            FlowchartNode(id="emotion_reflection", title="EMOTIONAL RESPONSE", label="emotion_choice_post",
                        x=500, y=300),
            
            FlowchartNode(id="scene3_2", title="EMPTY CLASSROOM", label="scene3_2",
                        x=800, y=300, major=True),
            
            FlowchartNode(id="isolation_choice", title="ISOLATION RESPONSE", label="isolation_post_choice",
                        x=1100, y=300),
            
            FlowchartNode(id="system_root", title="SYSTEM PROMPT", label="system_root_post_choice",
                        x=1400, y=300, major=True, completion_rate=30)
        ]

        # Branch nodes (emotional responses)
        branch_nodes = [
            FlowchartNode(id="feeling_guilt", title="GUILT", label="emotion_choice_guilt",
                        x=500, y=150),
            
            FlowchartNode(id="feeling_resigned", title="RESIGNATION", label="emotion_choice_resigned",
                        x=500, y=450),
            
            FlowchartNode(id="feeling_focused", title="FOCUS", label="emotion_choice_focused",
                        x=500, y=250),
            
            FlowchartNode(id="action_notes", title="KEEP WORKING", label="isolation_choice_notes",
                        x=1100, y=150),
            
            FlowchartNode(id="action_look", title="OBSERVE", label="isolation_choice_look",
                        x=1100, y=250),
            
            FlowchartNode(id="action_text", title="REACH OUT", label="isolation_choice_text",
                        x=1100, y=350),
            
            FlowchartNode(id="system_accept", title="ENTER SYSTEM", label="system_root_accept",
                        x=1400, y=150, node_type="secret"),
            
            FlowchartNode(id="system_ignore", title="IGNORE PROMPT", label="system_root_ignore",
                        x=1400, y=450)
        ]

        # Add all nodes
        for node in core_nodes + branch_nodes:
            flowchart.add_node(node)

        # Connections
        connections = [
            # Main path
            ("scene3_1_5", "emotion_reflection", "linear", 
            {"impact_type": "reflection", "magnitude": 2, "feedback_text": "Reflecting on disappearing friends"}),
            
            ("emotion_reflection", "scene3_2", "linear",
            {"impact_type": "glitches", "magnitude": 1, "feedback_text": "Entering empty classroom"}),
            
            ("scene3_2", "isolation_choice", "linear",
            {"impact_type": "reflection", "magnitude": 1.5, "feedback_text": "Confronting isolation"}),
            
            ("isolation_choice", "system_root", "conditional",
            {"impact_type": "glitches", "magnitude": 1, "feedback_text": "System prompt appears", "condition": "glitches >= 4"}),
            
            # Emotional branches
            ("emotion_reflection", "feeling_guilt", "choice",
            {"impact_type": "reflection", "magnitude": 1.5, "feedback_text": "Chose guilt response"}),
            
            ("emotion_reflection", "feeling_resigned", "choice",
            {"impact_type": "reflection", "magnitude": 0.5, "feedback_text": "Chose resignation"}),
            
            ("emotion_reflection", "feeling_focused", "choice",
            {"impact_type": "reflection", "magnitude": 1.0, "feedback_text": "Chose focus"}),
            
            # Isolation actions
            ("isolation_choice", "action_notes", "choice",
            {"impact_type": "glitches", "magnitude": 1, "feedback_text": "Kept taking notes"}),
            
            ("isolation_choice", "action_look", "choice",
            {"impact_type": "remembering", "magnitude": 0.5, "feedback_text": "Looked around"}),
            
            ("isolation_choice", "action_text", "choice",
            {"impact_type": "relationships", "magnitude": 1, "feedback_text": "Tried contacting friends"}),
            
            # System choices
            ("system_root", "system_accept", "secret",
            {"impact_type": "glitches", "magnitude": 2, "feedback_text": "Entered system settings"}),
            
            ("system_root", "system_ignore", "choice",
            {"impact_type": "reflection", "magnitude": 0.5, "feedback_text": "Ignored the prompt"})
        ]

        for src, dest, conn_type, data in connections:
            flowchart.nodes[src].add_connection(dest, connection_type=conn_type, choice_data=data)

        return flowchart
    def init_act3_quiz_flowchart():
        flowchart = Flowchart("Act 3: Framework Quiz")

        # Position constants
        COLUMN_SPACING = 300
        ROW_SPACING = 150
        BRANCH_OFFSET = 200

        # Core nodes
        core_nodes = [
            FlowchartNode(id="scene3_3", title="FRAMEWORK LECTURE", label="scene3_3", 
                        x=200, y=300, major=True, completion_rate=15),
            
            FlowchartNode(id="quiz_start", title="QUIZ BEGINS", label="scene3_3_quiz",
                        x=500, y=300, major=True),
            
            FlowchartNode(id="quiz_results", title="QUIZ RESULTS", label="ml_quiz_results",
                        x=2000, y=300, major=True, completion_rate=30)
        ]

        # Quiz question nodes
        quiz_nodes = [
            FlowchartNode(id="q1", title="DATA REQUIREMENTS", label="ml_quiz_1_correct",
                        x=800, y=100),
            
            FlowchartNode(id="q1_wrong", title="INCORRECT Q1", label="ml_quiz_1_wrong",
                        x=800, y=250),
            
            FlowchartNode(id="q2", title="FRAMEWORK ID", label="ml_quiz_2_correct",
                        x=1100, y=100),
            
            FlowchartNode(id="q2_wrong", title="INCORRECT Q2", label="ml_quiz_2_wrong",
                        x=1100, y=250),
            
            FlowchartNode(id="q3", title="SUPERVISED LIMITS", label="ml_quiz_3_correct",
                        x=1400, y=100),
            
            FlowchartNode(id="q3_wrong", title="INCORRECT Q3", label="ml_quiz_3_wrong",
                        x=1400, y=250),
            
            FlowchartNode(id="q4", title="REINFORCEMENT USE", label="ml_quiz_4_correct",
                        x=1700, y=100),
            
            FlowchartNode(id="q4_wrong", title="INCORRECT Q4", label="ml_quiz_4_wrong",
                        x=1700, y=250)
        ]

        # Add all nodes
        for node in core_nodes + quiz_nodes:
            flowchart.add_node(node)

        # Connections
        connections = [
            # Main path
            ("scene3_3", "quiz_start", "linear", 
            {"impact_type": "knowledge", "magnitude": 2, "feedback_text": "Framework lecture concludes"}),
            
            ("quiz_start", "q1", "quiz", 
            {"impact_type": "knowledge", "magnitude": 1, "feedback_text": "Question 1: Data requirements"}),
            
            # Question 1 branches
            ("q1", "q2", "linear",
            {"impact_type": "knowledge", "magnitude": 1, "feedback_text": "Correct answer"}),
            
            ("q1_wrong", "q2", "linear",
            {"impact_type": "knowledge", "magnitude": -0.5, "feedback_text": "Incorrect answer"}),
            
            # Question 2 branches
            ("q2", "q3", "linear",
            {"impact_type": "knowledge", "magnitude": 1, "feedback_text": "Correct answer"}),
            
            ("q2_wrong", "q3", "linear",
            {"impact_type": "knowledge", "magnitude": -0.5, "feedback_text": "Incorrect answer"}),
            
            # Question 3 branches
            ("q3", "q4", "linear",
            {"impact_type": "knowledge", "magnitude": 1, "feedback_text": "Correct answer"}),
            
            ("q3_wrong", "q4", "linear",
            {"impact_type": "knowledge", "magnitude": -0.5, "feedback_text": "Incorrect answer"}),
            
            # Question 4 to results
            ("q4", "quiz_results", "linear",
            {"impact_type": "knowledge", "magnitude": 1, "feedback_text": "Final question complete"}),
            
            ("q4_wrong", "quiz_results", "linear",
            {"impact_type": "knowledge", "magnitude": -0.5, "feedback_text": "Final question missed"})
        ]

        for src, dest, conn_type, data in connections:
            flowchart.nodes[src].add_connection(dest, connection_type=conn_type, choice_data=data)

        return flowchart
        