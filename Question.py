


QUESTIONS = [

    # AGE 1

    {
        "id": 1,
        "age": 1,
        "flag": None,
        "flag_value": None,
        "question": "Your baby cries frequently during the night. You are exhausted.",
        "choices": {
            "A": {
                "text": "Get up and comfort the baby every time.",
                "effects": {"parental_neglect": -1},
                "flags": {}
            },
            "B": {
                "text": "Comfort the baby most times but let them settle occasionally.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Leave the baby to cry. You need sleep.",
                "effects": {"parental_neglect": 2, "mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 2,
        "age": 1,
        "flag": None,
        "flag_value": None,
        "question": "The baby has a vaccination appointment. It is a busy week for you.",
        "choices": {
            "A": {
                "text": "Take the baby on time. Health comes first.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Reschedule for next week.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Skip it. You will go when things calm down.",
                "effects": {"parental_neglect": 2},
                "flags": {}
            }
        }
    },

    # AGE 2

    {
        "id": 3,
        "age": 2,
        "flag": None,
        "flag_value": None,
        "question": "Your child knocks over and breaks something at home by accident.",
        "choices": {
            "A": {
                "text": "Calmly explain why we have to be careful with things.",
                "effects": {"impulsivity_score": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them off briefly and move on.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Shout and make the child feel bad about it.",
                "effects": {"abuse": 1, "mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 4,
        "age": 2,
        "flag": None,
        "flag_value": None,
        "question": "Your child wants to play with other children at the park but is shy.",
        "choices": {
            "A": {
                "text": "Gently encourage them and stay close while they approach other kids.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Let them figure it out on their own.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them to stop being shy and push them toward the group.",
                "effects": {"mental_health_score": -1, "impulsivity_score": 1},
                "flags": {}
            }
        }
    },

    # AGE 3

    {
        "id": 5,
        "age": 3,
        "flag": None,
        "flag_value": None,
        "question": "Money is tight this month. The child asks for a toy they saw at the shop.",
        "choices": {
            "A": {
                "text": "Explain simply that you cannot afford it right now.",
                "effects": {},
                "flags": {}
            },
            "B": {
                "text": "Buy it anyway. You do not want the child to feel left out.",
                "effects": {"household_instability": 1},
                "flags": {}
            },
            "C": {
                "text": "Snap at the child for asking. The financial stress is getting to you.",
                "effects": {"abuse": 1, "mental_health_score": -1, "household_instability": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 6,
        "age": 3,
        "flag": None,
        "flag_value": None,
        "question": "Your child asks a lot of questions about everything. It gets tiring.",
        "choices": {
            "A": {
                "text": "Answer patiently. Curiosity is a good sign.",
                "effects": {"mental_health_score": 1, "school_neglect": -1},
                "flags": {}
            },
            "B": {
                "text": "Answer sometimes but tell them to be quiet other times.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them to stop asking so many questions.",
                "effects": {"mental_health_score": -1, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

    # AGE 4

    {
        "id": 7,
        "age": 4,
        "flag": None,
        "flag_value": None,
        "question": "There is a free preschool programme available in your area.",
        "choices": {
            "A": {
                "text": "Enrol the child. It is a great opportunity.",
                "effects": {"school_neglect": -2, "mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Consider it but do not commit yet.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Skip it. They are too young to need structured learning.",
                "effects": {"school_neglect": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 8,
        "age": 4,
        "flag": None,
        "flag_value": None,
        "question": "Your child throws a loud tantrum in a supermarket when you say no to sweets.",
        "choices": {
            "A": {
                "text": "Stay calm, get down to their level, and wait for them to settle.",
                "effects": {"impulsivity_score": -1},
                "flags": {}
            },
            "B": {
                "text": "Give them the sweets to stop the scene.",
                "effects": {"impulsivity_score": 1},
                "flags": {}
            },
            "C": {
                "text": "Grab them and leave, shouting as you go.",
                "effects": {"abuse": 1, "impulsivity_score": 1},
                "flags": {}
            }
        }
    },

    # AGE 5 - MAJOR BRANCH: in_school and family_stable

    {
        "id": 9,
        "age": 5,
        "flag": None,
        "flag_value": None,
        "question": "It is time for school. What do you decide?",
        "choices": {
            "A": {
                "text": "Enrol the child in the local school on time.",
                "effects": {},
                "flags": {"in_school": True}
            },
            "B": {
                "text": "Delay enrolment by a year. They seem too young.",
                "effects": {"school_neglect": 2},
                "flags": {"in_school": False}
            },
            "C": {
                "text": "Keep them home. You will manage their learning yourself.",
                "effects": {"school_neglect": 1},
                "flags": {"in_school": False}
            }
        }
    },

    {
        "id": 10,
        "age": 5,
        "flag": None,
        "flag_value": None,
        "question": "Your child ignores a rule you set, like not running inside. How do you handle it?",
        "choices": {
            "A": {
                "text": "Calmly remind them of the rule and explain why it exists.",
                "effects": {"impulsivity_score": -1},
                "flags": {}
            },
            "B": {
                "text": "Give them a warning and let it go this time.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Punish them harshly. Rules are rules.",
                "effects": {"abuse": 1, "mental_health_score": -1},
                "flags": {}
            }
        }
    },

    # AGE 6

    {
        "id": 11,
        "age": 6,
        "flag": None,
        "flag_value": None,
        "question": "Your child is struggling with reading. They fall behind the rest of the class.",
        "choices": {
            "A": {
                "text": "Read with them every evening and speak to the teacher.",
                "effects": {"school_neglect": -2},
                "flags": {}
            },
            "B": {
                "text": "Encourage them to try harder but take no extra steps.",
                "effects": {"school_neglect": 1},
                "flags": {}
            },
            "C": {
                "text": "Ignore the issue. They will catch up eventually.",
                "effects": {"school_neglect": 2, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 12,
        "age": 6,
        "flag": None,
        "flag_value": None,
        "question": "Your child comes home excited. They have made their first close friend at school.",
        "choices": {
            "A": {
                "text": "Invite the friend over and get to know them.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Encourage the friendship but do not get involved.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell the child to focus on schoolwork, not socialising.",
                "effects": {"mental_health_score": -1, "peer_delinquency": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 13,
        "age": 6,
        "flag": None,
        "flag_value": None,
        "question": "Work is very demanding this month. You are rarely home before the child's bedtime.",
        "choices": {
            "A": {
                "text": "Talk to your manager about flexible hours. Family comes first.",
                "effects": {"parental_neglect": -1},
                "flags": {}
            },
            "B": {
                "text": "Push through. Things will settle down soon.",
                "effects": {"parental_neglect": 1},
                "flags": {}
            },
            "C": {
                "text": "Accept the situation. You need the money.",
                "effects": {"parental_neglect": 2, "household_instability": 1},
                "flags": {}
            }
        }
    },

    # AGE 7

    {
        "id": 14,
        "age": 7,
        "flag": None,
        "flag_value": None,
        "question": "Your child lies to you about having finished their homework to go and play.",
        "choices": {
            "A": {
                "text": "Sit down with them, talk about honesty, and check the homework together.",
                "effects": {"school_neglect": -1, "impulsivity_score": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them off and send them to finish it.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Let it go this time. It is just homework.",
                "effects": {"school_neglect": 2, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 15,
        "age": 7,
        "flag": None,
        "flag_value": None,
        "question": "Your child follows you around the house wanting attention after school. You are tired.",
        "choices": {
            "A": {
                "text": "Put other things aside and spend 20 minutes with them.",
                "effects": {"parental_neglect": -1, "mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to play quietly for a bit while you rest.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Send them to their room. You need peace and quiet.",
                "effects": {"parental_neglect": 2, "mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 16,
        "age": 7,
        "flag": None,
        "flag_value": None,
        "question": "Your child comes home upset after a physical fight with another child in the street.",
        "choices": {
            "A": {
                "text": "Listen to what happened, then talk about better ways to handle conflict.",
                "effects": {"impulsivity_score": -1, "mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to avoid that child from now on.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them they should have hit back harder.",
                "effects": {"impulsivity_score": 2, "peer_delinquency": 1},
                "flags": {}
            }
        }
    },

    # AGE 8 - BRANCH: in_school

    # -- School path --

    {
        "id": 17,
        "age": 8,
        "flag": "in_school",
        "flag_value": True,
        "question": "The teacher contacts you. Your child's grades have been dropping this term.",
        "choices": {
            "A": {
                "text": "Meet the teacher and make a plan together.",
                "effects": {"school_neglect": -2, "parental_neglect": -1},
                "flags": {}
            },
            "B": {
                "text": "Talk to the child at home and tell them to try harder.",
                "effects": {"school_neglect": -1},
                "flags": {}
            },
            "C": {
                "text": "Do not respond. The school will handle it.",
                "effects": {"school_neglect": 2, "parental_neglect": 2},
                "flags": {}
            }
        }
    },

    {
        "id": 18,
        "age": 8,
        "flag": "in_school",
        "flag_value": True,
        "question": "Your child tells you another child at school has been calling them names and pushing them.",
        "choices": {
            "A": {
                "text": "Contact the school right away and support your child.",
                "effects": {"abuse": -1, "mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Tell your child to ignore it and walk away.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them to stand up and push back. Do not let anyone walk over you.",
                "effects": {"impulsivity_score": 1, "peer_delinquency": 1},
                "flags": {}
            }
        }
    },

    # -- Non-school path --

    {
        "id": 19,
        "age": 8,
        "flag": "in_school",
        "flag_value": False,
        "question": "Your child spends most of the day alone at home while you work.",
        "choices": {
            "A": {
                "text": "Arrange a childminder or neighbour to check in regularly.",
                "effects": {"parental_neglect": -1},
                "flags": {}
            },
            "B": {
                "text": "Leave them a list of tasks and activities to do.",
                "effects": {"parental_neglect": 1},
                "flags": {}
            },
            "C": {
                "text": "Leave them to manage. They are old enough.",
                "effects": {"parental_neglect": 2, "household_instability": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 20,
        "age": 8,
        "flag": "in_school",
        "flag_value": False,
        "question": "You realise your child cannot read at the level expected for their age.",
        "choices": {
            "A": {
                "text": "Dedicate time each day to reading practice.",
                "effects": {"school_neglect": -2},
                "flags": {}
            },
            "B": {
                "text": "Buy some books and hope they pick it up.",
                "effects": {"school_neglect": 1},
                "flags": {}
            },
            "C": {
                "text": "Do not worry about it. Formal reading is not everything.",
                "effects": {"school_neglect": 3},
                "flags": {}
            }
        }
    },

    # AGE 9

    {
        "id": 21,
        "age": 9,
        "flag": None,
        "flag_value": None,
        "question": "Your child asks for a smartphone. Most of their friends already have one.",
        "choices": {
            "A": {
                "text": "Get them a basic phone with parental controls.",
                "effects": {},
                "flags": {}
            },
            "B": {
                "text": "Tell them they can have one at 12.",
                "effects": {"mental_health_score": -1},
                "flags": {}
            },
            "C": {
                "text": "Get them a full smartphone with no restrictions.",
                "effects": {"impulsivity_score": 1, "school_neglect": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 22,
        "age": 9,
        "flag": None,
        "flag_value": None,
        "question": "You are offered a better job but it means moving to a different city.",
        "choices": {
            "A": {
                "text": "Decline. Uprooting the child now would cause too much disruption.",
                "effects": {},
                "flags": {}
            },
            "B": {
                "text": "Accept and involve the child in the move as much as possible.",
                "effects": {"household_instability": 1},
                "flags": {}
            },
            "C": {
                "text": "Accept and move quickly. The child will adapt.",
                "effects": {"household_instability": 2, "mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 23,
        "age": 9,
        "flag": None,
        "flag_value": None,
        "question": "Your child says they are stupid compared to their classmates.",
        "choices": {
            "A": {
                "text": "Reassure them and talk about effort versus ability.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to work harder and stop comparing themselves.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Agree they need to do better and leave it at that.",
                "effects": {"mental_health_score": -2, "school_neglect": 1},
                "flags": {}
            }
        }
    },

    # AGE 10
    

    {
        "id": 24,
        "age": 10,
        "flag": None,
        "flag_value": None,
        "question": "Your child is caught copying answers from a classmate during a test.",
        "choices": {
            "A": {
                "text": "Talk about integrity and why shortcuts create bigger problems later.",
                "effects": {"school_neglect": -1, "impulsivity_score": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them off and take away screen time for a week.",
                "effects": {"impulsivity_score": -1},
                "flags": {}
            },
            "C": {
                "text": "Tell them to be more careful next time so they do not get caught.",
                "effects": {"impulsivity_score": 1, "school_neglect": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 25,
        "age": 10,
        "flag": None,
        "flag_value": None,
        "question": "Your child has started avoiding chores and small responsibilities around the house.",
        "choices": {
            "A": {
                "text": "Sit down and explain that everyone in the family has to contribute.",
                "effects": {"impulsivity_score": -1},
                "flags": {}
            },
            "B": {
                "text": "Do the chores yourself. It is not worth the argument.",
                "effects": {"parental_neglect": 1},
                "flags": {}
            },
            "C": {
                "text": "Ignore it. Chores are not that important at this age.",
                "effects": {"impulsivity_score": 1, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 26,
        "age": 10,
        "flag": None,
        "flag_value": None,
        "question": "An unexpected bill means the family has almost no money this month.",
        "choices": {
            "A": {
                "text": "Be honest with the child. Explain the situation simply.",
                "effects": {"household_instability": 1, "mental_health_score": 0},
                "flags": {}
            },
            "B": {
                "text": "Handle it quietly. The child does not need to know.",
                "effects": {"household_instability": 1},
                "flags": {}
            },
            "C": {
                "text": "Take out a loan and keep spending as normal.",
                "effects": {"household_instability": 2},
                "flags": {"family_stable": False}
            }
        }
    },

    # AGE 11 - MAJOR BRANCH: high_risk_peers
    

    {
        "id": 27,
        "age": 11,
        "flag": None,
        "flag_value": None,
        "question": "Your child has started spending time with a group that includes older teenagers.",
        "choices": {
            "A": {
                "text": "Invite them over so you can see what the group is like.",
                "effects": {"peer_delinquency": 1},
                "flags": {}
            },
            "B": {
                "text": "Set clear rules about when and where your child can meet them.",
                "effects": {},
                "flags": {"high_risk_peers": False}
            },
            "C": {
                "text": "Say nothing. They need to find their own friends.",
                "effects": {"peer_delinquency": 2},
                "flags": {"high_risk_peers": True}
            }
        }
    },

    {
        "id": 28,
        "age": 11,
        "flag": None,
        "flag_value": None,
        "question": "Your child wants to spend more time outside the home after school and on weekends.",
        "choices": {
            "A": {
                "text": "Allow it but ask them to check in and let you know where they are.",
                "effects": {},
                "flags": {}
            },
            "B": {
                "text": "Restrict outdoor time to weekends only.",
                "effects": {"mental_health_score": -1},
                "flags": {}
            },
            "C": {
                "text": "Let them go whenever they want. You trust them.",
                "effects": {"parental_neglect": 1, "peer_delinquency": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 29,
        "age": 11,
        "flag": None,
        "flag_value": None,
        "question": "Your child has started talking back and refusing small requests around the house.",
        "choices": {
            "A": {
                "text": "Stay calm, have a conversation about respect, and hold the boundary.",
                "effects": {"impulsivity_score": -1},
                "flags": {}
            },
            "B": {
                "text": "Let it go for now. It is probably just a phase.",
                "effects": {"impulsivity_score": 1},
                "flags": {}
            },
            "C": {
                "text": "React with anger. You are not going to be spoken to like that.",
                "effects": {"abuse": 1, "household_instability": 1},
                "flags": {}
            }
        }
    },

    # AGE 12 - BRANCH: high_risk_peers

    # -- High risk peer path --

    {
        "id": 30,
        "age": 12,
        "flag": "high_risk_peers",
        "flag_value": True,
        "question": "You find out some of your child's friends have been skipping school regularly.",
        "choices": {
            "A": {
                "text": "Talk to your child directly about it and monitor their attendance.",
                "effects": {"school_neglect": -1, "peer_delinquency": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to stay away from those kids.",
                "effects": {"peer_delinquency": -1},
                "flags": {}
            },
            "C": {
                "text": "Do nothing. You cannot control who they are friends with.",
                "effects": {"school_neglect": 1, "peer_delinquency": 2},
                "flags": {}
            }
        }
    },

    {
        "id": 31,
        "age": 12,
        "flag": "high_risk_peers",
        "flag_value": True,
        "question": "Your child tells you their friends dared them to scratch a car in the car park.",
        "choices": {
            "A": {
                "text": "Use this as a serious conversation about peer pressure and consequences.",
                "effects": {"impulsivity_score": -1, "peer_delinquency": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them it was wrong and restrict who they see for a while.",
                "effects": {"peer_delinquency": -1},
                "flags": {}
            },
            "C": {
                "text": "Laugh it off. Kids do stupid things.",
                "effects": {"impulsivity_score": 1, "peer_delinquency": 2},
                "flags": {}
            }
        }
    },

    # -- Low risk peer path --

    {
        "id": 32,
        "age": 12,
        "flag": "high_risk_peers",
        "flag_value": False,
        "question": "A local sports club invites your child to join their junior team.",
        "choices": {
            "A": {
                "text": "Encourage them and offer to help with transport.",
                "effects": {"mental_health_score": 1, "peer_delinquency": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them it is up to them.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them it will take too much time away from school.",
                "effects": {"mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 33,
        "age": 12,
        "flag": "high_risk_peers",
        "flag_value": False,
        "question": "Your child is nervous about entering a school academic competition.",
        "choices": {
            "A": {
                "text": "Help them prepare and tell them you are proud regardless of the result.",
                "effects": {"mental_health_score": 1, "school_neglect": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to enter and see what happens.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them not to bother if they are not confident.",
                "effects": {"mental_health_score": -1, "school_neglect": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 34,
        "age": 12,
        "flag": "high_risk_peers",
        "flag_value": False,
        "question": "Your child asks you a direct question: do you trust them?",
        "choices": {
            "A": {
                "text": "Tell them yes and explain what trust looks like in your household.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Say mostly, and leave it at that.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them trust is earned and they have not earned it yet.",
                "effects": {"mental_health_score": -1, "household_instability": 1},
                "flags": {}
            }
        }
    },

    # AGE 13 - MAJOR BRANCH: mental_health_support

    {
        "id": 35,
        "age": 13,
        "flag": None,
        "flag_value": None,
        "question": "Your child has become very withdrawn. They stay in their room and rarely talk.",
        "choices": {
            "A": {
                "text": "Check in gently every day and arrange to speak to a counsellor.",
                "effects": {"mental_health_score": 2},
                "flags": {"mental_health_support": True}
            },
            "B": {
                "text": "Give them space but keep an eye on things.",
                "effects": {"mental_health_score": -1},
                "flags": {"mental_health_support": False}
            },
            "C": {
                "text": "Leave them alone. Teenagers need privacy.",
                "effects": {"mental_health_score": -2, "parental_neglect": 1},
                "flags": {"mental_health_support": False}
            }
        }
    },

    {
        "id": 36,
        "age": 13,
        "flag": None,
        "flag_value": None,
        "question": "Your child is very stressed about upcoming exams and says they cannot cope.",
        "choices": {
            "A": {
                "text": "Help them make a study schedule and remind them that grades are not everything.",
                "effects": {"school_neglect": -1, "mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to focus and work harder.",
                "effects": {"school_neglect": -1},
                "flags": {}
            },
            "C": {
                "text": "Tell them stop complaining. Everyone finds school hard.",
                "effects": {"mental_health_score": -2, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 37,
        "age": 13,
        "flag": None,
        "flag_value": None,
        "question": "Your child is upset after a falling-out with a friend that started over something posted online.",
        "choices": {
            "A": {
                "text": "Listen to the full story before saying anything.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to stay off social media for a week.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Dismiss it. Online drama is not real life.",
                "effects": {"mental_health_score": -1, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

    # AGE 14 - BRANCH: mental_health_support

    # -- Support path --

    {
        "id": 38,
        "age": 14,
        "flag": "mental_health_support",
        "flag_value": True,
        "question": "Your child's counsellor says they are making progress but needs to keep attending sessions.",
        "choices": {
            "A": {
                "text": "Keep the sessions going. The investment is worth it.",
                "effects": {"mental_health_score": 2},
                "flags": {}
            },
            "B": {
                "text": "Continue for now but review in a month.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "C": {
                "text": "Stop. They seem fine now and it is getting expensive.",
                "effects": {"mental_health_score": -1},
                "flags": {"mental_health_support": False}
            }
        }
    },

    # -- No support path --

    {
        "id": 39,
        "age": 14,
        "flag": "mental_health_support",
        "flag_value": False,
        "question": "Your child seems increasingly lonely and says they have no one to talk to.",
        "choices": {
            "A": {
                "text": "Take it seriously and suggest speaking to someone outside the family.",
                "effects": {"mental_health_score": 2},
                "flags": {"mental_health_support": True}
            },
            "B": {
                "text": "Tell them to make more effort with friends.",
                "effects": {"mental_health_score": -1},
                "flags": {}
            },
            "C": {
                "text": "Ignore it. They are being dramatic.",
                "effects": {"mental_health_score": -2, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 40,
        "age": 14,
        "flag": None,
        "flag_value": None,
        "question": "Your child has started their first romantic relationship. They are spending a lot of time with this person.",
        "choices": {
            "A": {
                "text": "Talk to them about healthy relationships and set reasonable expectations.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Let them figure it out. It is a normal part of growing up.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Forbid it completely. They are too young.",
                "effects": {"household_instability": 1, "mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 41,
        "age": 14,
        "flag": None,
        "flag_value": None,
        "question": "Your child says they dress differently to fit in with a new group at school.",
        "choices": {
            "A": {
                "text": "Talk about self-expression and how peer pressure works.",
                "effects": {"peer_delinquency": -1},
                "flags": {}
            },
            "B": {
                "text": "Let them dress how they want. It is harmless.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them they look ridiculous and make them change.",
                "effects": {"mental_health_score": -1, "household_instability": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 42,
        "age": 14,
        "flag": None,
        "flag_value": None,
        "question": "You notice your child is watching a lot of online content you are not comfortable with.",
        "choices": {
            "A": {
                "text": "Sit with them and discuss what they are watching and why.",
                "effects": {"parental_neglect": -1, "impulsivity_score": -1},
                "flags": {}
            },
            "B": {
                "text": "Block the content and say nothing.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Do nothing. It is just videos.",
                "effects": {"impulsivity_score": 1, "peer_delinquency": 1},
                "flags": {}
            }
        }
    },

    # AGE 15 - BRANCH: high_risk_peers

    # -- High risk peer path --

    {
        "id": 43,
        "age": 15,
        "flag": "high_risk_peers",
        "flag_value": True,
        "question": "Your child is invited to a party where you know there will be alcohol.",
        "choices": {
            "A": {
                "text": "Say no and explain why. Offer an alternative for the evening.",
                "effects": {"substance_exposure": 0},
                "flags": {}
            },
            "B": {
                "text": "Allow it but set a strict curfew and ask them to text you.",
                "effects": {"substance_exposure": 1},
                "flags": {}
            },
            "C": {
                "text": "Allow it without any conditions. They will be fine.",
                "effects": {"substance_exposure": 2, "peer_delinquency": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 44,
        "age": 15,
        "flag": "high_risk_peers",
        "flag_value": True,
        "question": "Your child tells you their friends want them to skip class and hang out.",
        "choices": {
            "A": {
                "text": "Firmly say no and follow up with the school.",
                "effects": {"school_neglect": -1, "peer_delinquency": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them it is their choice but warn them of the consequences.",
                "effects": {"school_neglect": 1},
                "flags": {}
            },
            "C": {
                "text": "Do not get involved. You cannot follow them everywhere.",
                "effects": {"school_neglect": 2, "peer_delinquency": 1},
                "flags": {}
            }
        }
    },

    # -- Low risk peer path --

    {
        "id": 45,
        "age": 15,
        "flag": "high_risk_peers",
        "flag_value": False,
        "question": "Your child is invited to volunteer at a local community project on weekends.",
        "choices": {
            "A": {
                "text": "Encourage them to go. It is good for them and looks good on a CV.",
                "effects": {"mental_health_score": 1, "peer_delinquency": -1},
                "flags": {}
            },
            "B": {
                "text": "Leave the decision to them.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them to use the time to study instead.",
                "effects": {"mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 46,
        "age": 15,
        "flag": "high_risk_peers",
        "flag_value": False,
        "question": "Your child is offered a small leadership role in a school club.",
        "choices": {
            "A": {
                "text": "Encourage them to take it. These experiences matter.",
                "effects": {"mental_health_score": 1, "school_neglect": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them it is their decision.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them not to take on extra stress when grades need to come first.",
                "effects": {"mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 47,
        "age": 15,
        "flag": None,
        "flag_value": None,
        "question": "There has been ongoing tension at home and it spills into a loud argument in front of the child.",
        "choices": {
            "A": {
                "text": "Apologise to the child for what they witnessed and talk it through later.",
                "effects": {"household_instability": -1, "mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Say nothing. Pretend it did not happen.",
                "effects": {"household_instability": 1},
                "flags": {}
            },
            "C": {
                "text": "The argument continues. Things at home feel very unstable.",
                "effects": {"household_instability": 2, "mental_health_score": -2},
                "flags": {"family_stable": False}
            }
        }
    },

    # AGE 16

    {
        "id": 48,
        "age": 16,
        "flag": None,
        "flag_value": None,
        "question": "Your child wants a part-time job. It would mean working evenings and some weekends.",
        "choices": {
            "A": {
                "text": "Support it but agree on a limit of hours so school does not suffer.",
                "effects": {"household_instability": -1},
                "flags": {}
            },
            "B": {
                "text": "Allow it with no conditions. They are old enough to manage.",
                "effects": {"school_neglect": 1},
                "flags": {}
            },
            "C": {
                "text": "Say no. School has to come first.",
                "effects": {"mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 49,
        "age": 16,
        "flag": None,
        "flag_value": None,
        "question": "Your child asks what you think they should do after school finishes.",
        "choices": {
            "A": {
                "text": "Have a real conversation about their interests and what options are available.",
                "effects": {"school_neglect": -1, "mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to figure it out. It is their life.",
                "effects": {"parental_neglect": 1},
                "flags": {}
            },
            "C": {
                "text": "Tell them to get a job as soon as possible. Education is not worth it.",
                "effects": {"school_neglect": 2},
                "flags": {}
            }
        }
    },

    {
        "id": 50,
        "age": 16,
        "flag": None,
        "flag_value": None,
        "question": "Your child tells you a close friend was caught shoplifting. The friend was not charged.",
        "choices": {
            "A": {
                "text": "Talk about what that means and what it says about that person's choices.",
                "effects": {"peer_delinquency": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to be careful about who they spend time with.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Say nothing. It is not your child who did it.",
                "effects": {"peer_delinquency": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 51,
        "age": 16,
        "flag": None,
        "flag_value": None,
        "question": "Your child says they feel completely overwhelmed and do not know how to cope.",
        "choices": {
            "A": {
                "text": "Take it seriously. Help them identify what is causing it and get support.",
                "effects": {"mental_health_score": 2},
                "flags": {"mental_health_support": True}
            },
            "B": {
                "text": "Listen and suggest some practical things they can try.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "C": {
                "text": "Tell them life is hard for everyone. They need to toughen up.",
                "effects": {"mental_health_score": -2, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

    # AGE 17

    {
        "id": 52,
        "age": 17,
        "flag": None,
        "flag_value": None,
        "question": "You find out your child has been drinking at gatherings with friends.",
        "choices": {
            "A": {
                "text": "Have a calm honest conversation about alcohol and its risks.",
                "effects": {"substance_exposure": -1},
                "flags": {}
            },
            "B": {
                "text": "Set a firm rule and ground them for two weeks.",
                "effects": {"substance_exposure": 0},
                "flags": {}
            },
            "C": {
                "text": "Let it go. At 17 it is practically unavoidable.",
                "effects": {"substance_exposure": 2},
                "flags": {}
            }
        }
    },

    {
        "id": 53,
        "age": 17,
        "flag": None,
        "flag_value": None,
        "question": "Your child's close friend group has changed. Some of the new friends seem unreliable.",
        "choices": {
            "A": {
                "text": "Ask your child about their new friends without making it an interrogation.",
                "effects": {"peer_delinquency": 0},
                "flags": {}
            },
            "B": {
                "text": "Say nothing. At 17 you cannot choose their friends for them.",
                "effects": {"peer_delinquency": 1},
                "flags": {}
            },
            "C": {
                "text": "Forbid them from seeing the new group.",
                "effects": {"household_instability": 1, "mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 54,
        "age": 17,
        "flag": None,
        "flag_value": None,
        "question": "A serious argument at home gets out of hand. Your child shouts that they hate living here.",
        "choices": {
            "A": {
                "text": "Cool down first, then have a real conversation about what led to it.",
                "effects": {"household_instability": -1, "mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Give each other space and hope it blows over.",
                "effects": {"household_instability": 1},
                "flags": {}
            },
            "C": {
                "text": "Shout back and tell them to leave if they feel that way.",
                "effects": {"household_instability": 2, "mental_health_score": -2, "abuse": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 55,
        "age": 17,
        "flag": None,
        "flag_value": None,
        "question": "You need your child to help look after a younger sibling regularly. It cuts into their free time.",
        "choices": {
            "A": {
                "text": "Ask them, explain the situation, and offer something in return.",
                "effects": {},
                "flags": {}
            },
            "B": {
                "text": "Tell them it is expected. Family helps family.",
                "effects": {"household_instability": 1, "mental_health_score": -1},
                "flags": {}
            },
            "C": {
                "text": "Demand it without explanation.",
                "effects": {"household_instability": 1, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

    # AGE 18

    {
        "id": 56,
        "age": 18,
        "flag": None,
        "flag_value": None,
        "question": "Your child finishes school. They are unsure whether to study further or start working.",
        "choices": {
            "A": {
                "text": "Sit down together and go through their real options without pushing your own opinion.",
                "effects": {"school_neglect": -1, "mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to get a job quickly. Bills do not wait.",
                "effects": {"school_neglect": 1},
                "flags": {}
            },
            "C": {
                "text": "Tell them to figure it out on their own. You have done your part.",
                "effects": {"parental_neglect": 2, "mental_health_score": -1},
                "flags": {}
            }
        }
    },

    {
        "id": 57,
        "age": 18,
        "flag": None,
        "flag_value": None,
        "question": "Your child tells you some of their friends are involved in things that sound illegal.",
        "choices": {
            "A": {
                "text": "Have a direct conversation. Ask if they are involved and why they are still around these people.",
                "effects": {"peer_delinquency": -1},
                "flags": {}
            },
            "B": {
                "text": "Tell them to distance themselves but leave it at that.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Say nothing. They are 18. It is not your responsibility anymore.",
                "effects": {"peer_delinquency": 2},
                "flags": {}
            }
        }
    },

    {
        "id": 58,
        "age": 18,
        "flag": None,
        "flag_value": None,
        "question": "Your child is moving toward independence. How much support do you offer?",
        "choices": {
            "A": {
                "text": "Stay involved and available. Let them lead but make clear you are there.",
                "effects": {"mental_health_score": 1, "parental_neglect": -1},
                "flags": {}
            },
            "B": {
                "text": "Step back but check in occasionally.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Cut back completely. They are an adult now.",
                "effects": {"parental_neglect": 2, "household_instability": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 59,
        "age": 18,
        "flag": None,
        "flag_value": None,
        "question": "Your child fails something important, a job application, a course, or an exam, and takes it badly.",
        "choices": {
            "A": {
                "text": "Acknowledge how hard it is and help them think through what comes next.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "B": {
                "text": "Tell them failure is normal and they should try again.",
                "effects": {},
                "flags": {}
            },
            "C": {
                "text": "Tell them you knew this would happen. They did not prepare enough.",
                "effects": {"mental_health_score": -2, "abuse": 1},
                "flags": {}
            }
        }
    },

    {
        "id": 60,
        "age": 18,
        "flag": None,
        "flag_value": None,
        "question": "Your child reflects on their upbringing and raises something that hurt them growing up.",
        "choices": {
            "A": {
                "text": "Listen fully without getting defensive. Acknowledge what they are saying.",
                "effects": {"mental_health_score": 2, "parental_neglect": -1},
                "flags": {}
            },
            "B": {
                "text": "Hear them out but explain your side as well.",
                "effects": {"mental_health_score": 1},
                "flags": {}
            },
            "C": {
                "text": "Tell them to stop living in the past and be grateful.",
                "effects": {"mental_health_score": -2, "abuse": 1, "parental_neglect": 1},
                "flags": {}
            }
        }
    },

]


def apply_effects(current_stats: dict, effects: dict) -> dict:
    """
    Apply effects to current_stats and ensure no stat goes below 0.

    Usage: from Question import apply_effects
    current_stats = apply_effects(current_stats, choice_effects)
    """
    for key, val in (effects or {}).items():
        # only apply numeric effects
        try:
            num = float(val)
        except Exception:
            continue
        current = current_stats.get(key, 0)
        try:
            new = current + val
        except Exception:
            # if val was float-convertible but not same type, coerce
            new = current + num
        # enforce minimum of 0
        if isinstance(new, (int, float)):
            if new < 0:
                new = 0
        current_stats[key] = new
    return current_stats

