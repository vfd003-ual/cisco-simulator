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
    {
        "id": 1006,
        "type": "checkbox",
        "question": "What are three characteristics of ASA transparent mode? (Choose three.)",
        "image": None,
        "options": [
            "This mode does not support VPNs, QoS, or DHCP Relay.",
            "It is the traditional firewall deployment mode.",
            "This mode is referred to as a \"bump in the wire.\"",
            "NAT can be implemented between connected networks.",
            "In this mode the ASA is invisible to an attacker.",
            "The interfaces of the ASA separate Layer 3 networks and require IP addresses in different subnets."
        ],
        "correct": [0, 2, 4],
        "explanation": "In transparent mode, the ASA acts as a Layer 2 device (bump in the wire), is invisible to attackers, and does not support VPNs, QoS, or DHCP Relay. The traditional firewall deployment mode is routed mode, not transparent mode."
    },
    {
        "id": 1007,
        "type": "radio",
        "question": "What is needed to allow specific traffic that is sourced on the outside network of an ASA firewall to reach an internal network?",
        "image": None,
        "options": [
            "ACL",
            "NAT",
            "dynamic routing protocols",
            "outside security zone level 0"
        ],
        "correct": [0],
        "explanation": "In order to explicitly permit traffic from an interface with a lower security level to an interface with a higher security level, an ACL must be configured. By default, traffic will only flow from a higher security level to a lower."
    },
    {
        "id": 1008,
        "type": "radio",
        "question": "What will be the result of failed login attempts if the following command is entered into a router?\n\nlogin block-for 150 attempts 4 within 90",
        "image": None,
        "options": [
            "All login attempts will be blocked for 150 seconds if there are 4 failed attempts within 90 seconds.",
            "All login attempts will be blocked for 90 seconds if there are 4 failed attempts within 150 seconds.",
            "All login attempts will be blocked for 1.5 hours if there are 4 failed attempts within 150 seconds.",
            "All login attempts will be blocked for 4 hours if there are 90 failed attempts within 150 seconds."
        ],
        "correct": [0],
        "explanation": "The components of the login block-for 150 attempts 4 within 90 command are as follows:\n- The expression block-for 150 is the time in seconds that logins will be blocked.\n- The expression attempts 4 is the number of failed attempts that will trigger the blocking of login requests.\n- The expression within 90 is the time in seconds in which the 4 failed attempts must occur."
    },
    {
        "id": 1009,
        "type": "checkbox",
        "question": "Which two tasks are associated with router hardening? (Choose two.)",
        "image": None,
        "options": [
            "placing the router in a secure room",
            "disabling unused ports and interfaces",
            "installing the maximum amount of memory possible",
            "securing administrative access",
            "using uninterruptible power supplies"
        ],
        "correct": [1, 3],
        "explanation": "Router hardening involves disabling unused ports and interfaces and securing administrative access. Physical security (secure room) and power supplies are infrastructure concerns, not specifically router hardening tasks."
    },
    {
        "id": 1010,
        "type": "radio",
        "question": "Which threat protection capability is provided by Cisco ESA?",
        "image": None,
        "options": [
            "web filtering",
            "cloud access security",
            "spam protection",
            "Layer 4 traffic monitoring"
        ],
        "correct": [2],
        "explanation": "Email is a top attack vector for security breaches. Cisco ESA includes many threat protection capabilities for email such as spam protection, forged email detection, and Cisco advanced phishing protection."
    },
]