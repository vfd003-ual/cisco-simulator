# Banco de preguntas Cisco Network Security - REAL

questions_real = [
    {
        "id": 1001,
        "type": "matching",
        "question": "Match the type of ASA ACLs to the description. (Not all options are used.)",
        "image": None,
        "left_items": [
            "standard access list",
            "extended access list",
            "EtherType access list",
            "webtype access list"
        ],
        "right_items": [
            "used to identify the destination IP addresses only",
            "used to specify source and destination addresses and protocol, ports, or the ICMP type",
            "used only if the security appliance is running in transparent mode",
            "used to support filtering for clientless SSL VPN",
            "used to determine which IPv6 traffic to block or to forward at router interfaces",
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "Place the options in the following order:\n- extended access lists: used to specify source and destination addresses and protocol, ports, or the ICMP type\n- webtype access lists: used to support filtering for clientless SSL VPN\n- standard access lists: used to identify the destination IP addresses only\n- EtherType access lists: used only if the security appliance is running in transparent mode"
    },
    {
        "id": 1002,
        "type": "radio",
        "question": "Which statement describes a difference between the Cisco ASA IOS CLI feature and the router IOS CLI feature?",
        "image": None,
        "options": [
            "ASA uses the ? command whereas a router uses the help command to receive help on a brief description and the syntax of a command.",
            "To use a show command in a general configuration mode, ASA can use the command directly whereas a router will need to enter the do command before issuing the show command.",
            "To complete a partially typed command, ASA uses the Ctrl+Tab key combination whereas a router uses the Tab key.",
            "To indicate the CLI EXEC mode, ASA uses the % symbol whereas a router uses the # symbol."
        ],
        "correct": [1],
        "explanation": "The ASA CLI is a proprietary OS which has a similar look and feel to the Cisco router IOS. Although it shares some common features with the router IOS, it has its unique features. For example, an ASA CLI command can be executed regardless of the current configuration mode prompt. The IOS do command is not required or recognized. Both the ASA CLI and the router CLI use the # symbol to indicate the EXEC mode. Both CLIs use the Tab key to complete a partially typed command. Different from the router IOS, the ASA provides a help command that provides a brief command description and syntax for certain commands."
    },
    {
        "id": 1003,
        "type": "radio",
        "question": "Refer to the exhibit. A network administrator is configuring AAA implementation on an ASA device. What does the option link3 indicate?",
        "image": "/static/images/1003.png",
        "options": [
            "the network name where the AAA server resides",
            "the specific AAA server name",
            "the sequence of servers in the AAA server group",
            "the interface name"
        ],
        "correct": [3],
        "explanation": "The option link3 indicates the interface name on the ASA device where the AAA server is connected."
    },
    {
        "id": 1004,
        "type": "radio",
        "question": "What provides both secure segmentation and threat defense in a Secure Data Center solution?",
        "image": None,
        "options": [
            "Cisco Security Manager software",
            "AAA server",
            "Adaptive Security Appliance",
            "intrusion prevention system"
        ],
        "correct": [2],
        "explanation": "The Adaptive Security Appliance (ASA) provides both secure segmentation and threat defense capabilities in a Secure Data Center solution."
    },
    {
        "id": 1005,
        "type": "checkbox",
        "question": "What are the three core components of the Cisco Secure Data Center solution? (Choose three.)",
        "image": None,
        "options": [
            "mesh network",
            "secure segmentation",
            "visibility",
            "threat defense",
            "servers",
            "infrastructure"
        ],
        "correct": [1, 2, 3],
        "explanation": "Secure segmentation is used when managing and organizing data in a data center. Threat defense includes a firewall and intrusion prevention system (IPS). Data center visibility is designed to simplify operations and compliance reporting by providing consistent security policy enforcement."
    },
]