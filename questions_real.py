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
    {
        "id": 1011,
        "type": "checkbox",
        "question": "What are two security measures used to protect endpoints in the borderless network? (Choose two.)",
        "image": None,
        "options": [
            "denylisting",
            "Snort IPS",
            "DLP",
            "DMZ",
            "rootkit"
        ],
        "correct": [0, 2],
        "explanation": "Security measures for endpoints:\n- antimalware software: Protect endpoints from malware.\n- spam filtering: Prevent spam emails from reaching endpoints.\n- blocklisting: Prevent endpoints from connecting to websites with bad reputations by immediately blocking connections based on the latest reputation intelligence.\n- data loss prevention (DLP): Prevent sensitive information from being lost or stolen."
    },
    {
        "id": 1012,
        "type": "checkbox",
        "question": "Which three types of traffic are allowed when the authentication port-control auto command has been issued and the client has not yet been authenticated? (Choose three.)",
        "image": None,
        "options": [
            "CDP",
            "802.1Q",
            "IPsec",
            "TACACS+",
            "STP",
            "EAPOL"
        ],
        "correct": [0, 4, 5],
        "explanation": "Until the workstation is authenticated, 802.1X access control enables only Extensible Authentication Protocol over LAN (EAPOL), Cisco Discovery Protocol (CDP), and Spanning Tree Protocol (STP) traffic through the port to which the workstation is connected. After authentication succeeds, normal traffic can pass through the port."
    },
    {
        "id": 1013,
        "type": "radio",
        "question": "Which statement describes a characteristic of the IKE protocol?",
        "image": None,
        "options": [
            "It uses UDP port 500 to exchange IKE information between the security gateways.",
            "IKE Phase 1 can be implemented in three different modes: main, aggressive, or quick.",
            "It allows for the transmission of keys directly across a network.",
            "The purpose of IKE Phase 2 is to negotiate a security association between two IKE peers."
        ],
        "correct": [0],
        "explanation": "IKE uses UDP port 500 to exchange IKE information between security gateways. Quick mode is part of Phase 2, not Phase 1. Keys are not transmitted directly; they are negotiated using Diffie-Hellman."
    },
    {
        "id": 1014,
        "type": "radio",
        "question": "Which action do IPsec peers take during the IKE Phase 2 exchange?",
        "image": None,
        "options": [
            "exchange of DH keys",
            "negotiation of IPsec policy",
            "negotiation of IKE policy sets",
            "verification of peer identity"
        ],
        "correct": [1],
        "explanation": "The IKE protocol executes in two phases. During Phase 1 the two sides negotiate IKE policy sets, authenticate each other, and set up a secure channel. During the second phase IKE negotiates security associations between the peers."
    },
    {
        "id": 1015,
        "type": "checkbox",
        "question": "What are two hashing algorithms used with IPsec AH to guarantee authenticity? (Choose two.)",
        "image": None,
        "options": [
            "SHA",
            "RSA",
            "DH",
            "MD5",
            "AES"
        ],
        "correct": [0, 3],
        "explanation": "The IPsec framework uses various protocols and algorithms to provide data confidentiality, data integrity, authentication, and secure key exchange. Two popular algorithms used to ensure that data is not intercepted and modified (data integrity and authenticity) are MD5 and SHA."
    },
    {
        "id": 1016,
        "type": "radio",
        "question": "Which command raises the privilege level of the ping command to 7?",
        "image": None,
        "options": [
            "user exec ping level 7",
            "authorization exec ping level 7",
            "accounting exec level 7 ping",
            "privilege exec level 7 ping"
        ],
        "correct": [3],
        "explanation": "The privilege exec level command is used to change the privilege level of a command. The syntax is: privilege exec level [level] [command]."
    },
    {
        "id": 1017,
        "type": "radio",
        "question": "What is a characteristic of a role-based CLI view of router configuration?",
        "image": None,
        "options": [
            "A CLI view has a command hierarchy, with higher and lower views.",
            "When a superview is deleted, the associated CLI views are deleted.",
            "A single CLI view can be shared within multiple superviews.",
            "Only a superview user can configure a new view and add or remove commands from the existing views."
        ],
        "correct": [2],
        "explanation": "A CLI view has no command hierarchy, and therefore, no higher or lower views. Deleting a superview does not delete the associated CLI views. Only a root view user can configure a new view and add or remove commands from the existing views."
    },
    {
        "id": 1018,
        "type": "radio",
        "question": "What is a limitation to using OOB management on a large enterprise network?",
        "image": None,
        "options": [
            "Production traffic shares the network with management traffic.",
            "Terminal servers can have direct console connections to user devices needing management.",
            "OOB management requires the creation of VPNs.",
            "All devices appear to be attached to a single management network."
        ],
        "correct": [3],
        "explanation": "OOB management provides a dedicated management network without production traffic. Devices within that network, such as terminal servers, have direct console access for management purposes. Because in-band management runs over the production network, secure tunnels or VPNs may be needed. Failures on the production network may not be communicated to the OOB network administrator because the OOB management network may not be affected."
    },
    {
        "id": 1019,
        "type": "radio",
        "question": "Refer to the exhibit. A corporate network is using NTP to synchronize the time across devices. What can be determined from the displayed output?",
        "image": "/static/images/1019.png",
        "options": [
            "Router03 is a stratum 2 device that can provide NTP service to other devices in the network.",
            "The time on Router03 may not be reliable because it is offset by more than 7 seconds to the time server.",
            "The interface on Router03 that connects to the time sever has the IPv4 address 209.165.200.225.",
            "Router03 time is synchronized to a stratum 2 time server."
        ],
        "correct": [0],
        "explanation": "The show ntp status command displays that Router03 is now a stratum 2 device synchronized with the NTP server at 209.165.220.225 and can provide NTP service to other devices in the network. The clock offset is only 7.0883 milliseconds, not 7.0883 seconds."
    },
    {
        "id": 1020,
        "type": "checkbox",
        "question": "Refer to the exhibit. Which two conclusions can be drawn from the syslog message that was generated by the router? (Choose two.)",
        "image": "/static/images/1020.jpg",
        "options": [
            "This message resulted from an unusual error requiring reconfiguration of the interface.",
            "This message indicates that service timestamps have been configured.",
            "This message indicates that the interface changed state five times.",
            "This message is a level 5 notification message.",
            "This message indicates that the interface should be replaced."
        ],
        "correct": [1, 3],
        "explanation": "The message is a level 5 notification message as shown in the %LINEPROTO-5 section of the output. Messages reporting the link status are common and do not require replacing the interface or reconfiguring the interface. The date and time displayed at the beginning of the message indicates that service timestamps have been configured on the router."
    },
    {
        "id": 1021,
        "type": "checkbox",
        "question": "Which two types of hackers are typically classified as grey hat hackers? (Choose two.)",
        "image": None,
        "options": [
            "hacktivists",
            "cyber criminals",
            "vulnerability brokers",
            "script kiddies",
            "state-sponsored hackers"
        ],
        "correct": [0, 2],
        "explanation": "Grey hat hackers may do unethical or illegal things, but not for personal gain or to cause damage. Hacktivists use their hacking as a form of political or social protest, and vulnerability brokers hack to uncover weaknesses and report them to vendors. Depending on the perspective one possesses, state-sponsored hackers are either white hat or black hat operators. Script kiddies create hacking scripts to cause damage or disruption. Cyber criminals use hacking to obtain financial gain by illegal means."
    },
    {
        "id": 1022,
        "type": "radio",
        "question": "When describing malware, what is a difference between a virus and a worm?",
        "image": None,
        "options": [
            "A virus focuses on gaining privileged access to a device, whereas a worm does not.",
            "A virus replicates itself by attaching to another file, whereas a worm can replicate itself independently.",
            "A virus can be used to launch a DoS attack (but not a DDoS), but a worm can be used to launch both DoS and DDoS attacks.",
            "A virus can be used to deliver advertisements without user consent, whereas a worm cannot."
        ],
        "correct": [1],
        "explanation": "Malware can be classified as follows:\n- Virus (self-replicates by attaching to another program or file)\n- Worm (replicates independently of another program)\n- Trojan horse (masquerades as a legitimate file or program)\n- Rootkit (gains privileged access to a machine while concealing itself)\n- Spyware (collects information from a target system)\n- Adware (delivers advertisements with or without consent)\n- Bot (waits for commands from the hacker)\n- Ransomware (holds a computer system or data captive until payment is received)"
    },
    {
        "id": 1023,
        "type": "radio",
        "question": "Which type of packet is unable to be filtered by an outbound ACL?",
        "image": None,
        "options": [
            "multicast packet",
            "ICMP packet",
            "broadcast packet",
            "router-generated packet"
        ],
        "correct": [3],
        "explanation": "Traffic that originates within a router such as pings from a command prompt, remote access from a router to another device, or routing updates are not affected by outbound access lists. The traffic must flow through the router in order for the router to apply the ACEs."
    },
    {
        "id": 1024,
        "type": "radio",
        "question": "Consider the access list command applied outbound on a router serial interface.\n\naccess-list 100 deny icmp 192.168.10.0 0.0.0.255 any echo reply\n\nWhat is the effect of applying this access list command?",
        "image": None,
        "options": [
            "The only traffic denied is echo-replies sourced from the 192.168.10.0/24 network. All other traffic is allowed.",
            "The only traffic denied is ICMP-based traffic. All other traffic is allowed.",
            "No traffic will be allowed outbound on the serial interface.",
            "Users on the 192.168.10.0/24 network are not allowed to transmit traffic to any other destination."
        ],
        "correct": [2],
        "explanation": "This ACL denies ICMP echo-replies from the 192.168.10.0/24 network. However, because there is an implicit deny all at the end of every ACL, and no permit statement is included, no traffic will be allowed outbound on the serial interface."
    },
    {
        "id": 1025,
        "type": "radio",
        "question": "Which command is used to activate an IPv6 ACL named ENG_ACL on an interface so that the router filters traffic prior to accessing the routing table?",
        "image": None,
        "options": [
            "ipv6 access-class ENG_ACL in",
            "ipv6 traffic-filter ENG_ACL out",
            "ipv6 traffic-filter ENG_ACL in",
            "ipv6 access-class ENG_ACL out"
        ],
        "correct": [2],
        "explanation": "For the purpose of applying an access list to a particular interface, the ipv6 traffic-filter IPv6 command is equivalent to the access-group IPv4 command. The direction in which the traffic is examined (in or out) is also required."
    },
    {
        "id": 1026,
        "type": "radio",
        "question": "What technology has a function of using trusted third-party protocols to issue credentials that are accepted as an authoritative identity?",
        "image": None,
        "options": [
            "digital signatures",
            "hashing algorithms",
            "PKI certificates",
            "symmetric keys"
        ],
        "correct": [2],
        "explanation": "Digital certificates are used to prove the authenticity and integrity of PKI certificates, but a PKI Certificate Authority is a trusted third-party entity that issues PKI certificates. PKI certificates are public information and are used to provide authenticity, confidentiality, integrity, and nonrepudiation services that can scale to large requirements."
    },
    {
        "id": 1027,
        "type": "checkbox",
        "question": "What are two methods to maintain certificate revocation status? (Choose two.)",
        "image": None,
        "options": [
            "subordinate CA",
            "OCSP",
            "DNS",
            "LDAP",
            "CRL"
        ],
        "correct": [1, 4],
        "explanation": "A digital certificate might need to be revoked if its key is compromised or it is no longer needed. The certificate revocation list (CRL) and Online Certificate Status Protocol (OCSP), are two common methods to check a certificate revocation status."
    },
    {
        "id": 1028,
        "type": "radio",
        "question": "Which protocol is an IETF standard that defines the PKI digital certificate format?",
        "image": None,
        "options": [
            "SSL/TLS",
            "X.500",
            "LDAP",
            "X.509"
        ],
        "correct": [3],
        "explanation": "To address the interoperability of different PKI vendors, IETF published the Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework (RFC 2527). The standard defines the format of a digital certificate."
    },
    {
        "id": 1029,
        "type": "radio",
        "question": "A network administrator is configuring DAI on a switch. Which command should be used on the uplink interface that connects to a router?",
        "image": None,
        "options": [
            "ip arp inspection trust",
            "ip dhcp snooping",
            "ip arp inspection vlan",
            "spanning-tree portfast"
        ],
        "correct": [0],
        "explanation": "In general, a router serves as the default gateway for the LAN or VLAN on the switch. Therefore, the uplink interface that connects to a router should be a trusted port for forwarding ARP requests."
    },
    {
        "id": 1030,
        "type": "radio",
        "question": "What is the best way to prevent a VLAN hopping attack?",
        "image": None,
        "options": [
            "Disable trunk negotiation for trunk ports and statically set nontrunk ports as access ports.",
            "Disable STP on all nontrunk ports.",
            "Use VLAN 1 as the native VLAN on trunk ports.",
            "Use ISL encapsulation on all trunk links."
        ],
        "correct": [0],
        "explanation": "VLAN hopping attacks rely on the attacker being able to create a trunk link with a switch. Disabling DTP and configuring user-facing ports as static access ports can help prevent these types of attacks. Disabling the Spanning Tree Protocol (STP) will not eliminate VLAN hopping attacks."
    },
    {
        "id": 1031,
        "type": "radio",
        "question": "What would be the primary reason an attacker would launch a MAC address overflow attack?",
        "image": None,
        "options": [
            "so that the switch stops forwarding traffic",
            "so that legitimate hosts cannot obtain a MAC address",
            "so that the attacker can see frames that are destined for other hosts",
            "so that the attacker can execute arbitrary code on the switch"
        ],
        "correct": [2],
        "explanation": "A MAC address overflow attack floods the switch with fake MAC addresses to fill the CAM table. When the table is full, the switch can no longer learn new MAC addresses and starts flooding traffic out all ports, allowing the attacker to see frames destined for other hosts."
    },
    {
        "id": 1032,
        "type": "radio",
        "question": "What is the main difference between the implementation of IDS and IPS devices?",
        "image": None,
        "options": [
            "An IDS can negatively impact the packet flow, whereas an IPS can not.",
            "An IDS needs to be deployed together with a firewall device, whereas an IPS can replace a firewall.",
            "An IDS would allow malicious traffic to pass before it is addressed, whereas an IPS stops it immediately.",
            "An IDS uses signature-based technology to detect malicious packets, whereas an IPS uses profile-based technology."
        ],
        "correct": [2],
        "explanation": "An IPS is deployed in inline mode and will not allow malicious traffic to enter the internal network without first analyzing it. An advantage of this is that it can stop an attack immediately. An IDS is deployed in promiscuous mode. It copies the traffic patterns and analyzes them offline, thus it cannot stop the attack immediately and it relies on another device to take further actions once it detects an attack. Being deployed in inline mode, an IPS can negatively impact the traffic flow. Both IDS and IPS can use signature-based technology to detect malicious packets. An IPS cannot replace other security devices, such as firewalls, because they perform different tasks."
    },
    {
        "id": 1033,
        "type": "radio",
        "question": "Which attack is defined as an attempt to exploit software vulnerabilities that are unknown or undisclosed by the vendor?",
        "image": None,
        "options": [
            "zero-day",
            "Trojan horse",
            "brute-force",
            "man-in-the-middle"
        ],
        "correct": [0],
        "explanation": "A zero-day attack exploits software vulnerabilities that are unknown or undisclosed by the vendor. These attacks are particularly dangerous because there are no patches or defenses available at the time of the attack."
    },
    {
        "id": 1034,
        "type": "matching",
        "question": "Match the network monitoring technology with the description.",
        "image": None,
        "left_items": [
            "passively monitors network traffic",
            "uses VLANs to monitor traffic on remote switches",
            "a passive traffic splitting device implemented inline between a device of interest and the network",
            "can perform a packet drop to stop the trigger packets"
        ],
        "right_items": [
            "RSPAN",
            "IDS",
            "IPS",
            "TAP"
        ],
        "correct": [1, 0, 3, 2],
        "explanation": "Place the options in the following order:\n- passively monitors network traffic: IDS\n- uses VLANs to monitor traffic on remote switches: RSPAN\n- a passive traffic splitting device implemented inline between a device of interest and the network: TAP\n- can perform a packet drop to stop the trigger packets: IPS"
    },
    {
        "id": 1035,
        "type": "checkbox",
        "question": "What are the three signature levels provided by Snort IPS on the 4000 Series ISR? (Choose three.)",
        "image": None,
        "options": [
            "security",
            "drop",
            "reject",
            "connectivity",
            "inspect",
            "balanced"
        ],
        "correct": [0, 3, 5],
        "explanation": "Snort IPS on the 4000 Series ISR provides three signature levels: security, connectivity, and balanced. These levels determine the trade-off between security protection and network performance."
    },
    {
        "id": 1036,
        "type": "checkbox",
        "question": "What are three attributes of IPS signatures? (Choose three.)",
        "image": None,
        "options": [
            "action",
            "length",
            "trigger",
            "type",
            "depth",
            "function"
        ],
        "correct": [0, 2, 3],
        "explanation": "IPS signatures have three distinctive attributes:\n- type\n- trigger (alarm)\n- action"
    },
    {
        "id": 1037,
        "type": "matching",
        "question": "Match each IPS signature trigger category with the description.",
        "image": None,
        "left_items": [
            "pattern-based detection",
            "anomaly-based detection",
            "policy-based detection",
            "honey pot-based detection"
        ],
        "right_items": [
            "simplest triggering mechanism which searches for a specific and pre-defined atomic or composite pattern",
            "involves first defining a profile of what is considered normal network or host activity",
            "requires an administrator to manually define behaviors that are suspicious based on historical analysis",
            "uses a decoy server to divert attacks away from production devices"
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "(ESTA PREGUNTA PUEDE APARECER EN VARIOS FORMATOS)\nIPS signature trigger categories:\n- pattern-based detection: simplest triggering mechanism which searches for a specific and pre-defined atomic or composite pattern\n- anomaly-based detection: involves first defining a profile of what is considered normal network or host activity\n- policy-based detection: requires an administrator to manually define behaviors that are suspicious based on historical analysis\n- honey pot-based detection: uses a decoy server to divert attacks away from production devices"
    },
    {
        "id": 1038,
        "type": "checkbox",
        "question": "Which two features are included by both TACACS+ and RADIUS protocols? (Choose two.)",
        "image": None,
        "options": [
            "SIP support",
            "password encryption",
            "802.1X support",
            "separate authentication and authorization processes",
            "utilization of transport layer protocols"
        ],
        "correct": [1, 4],
        "explanation": "Both TACACS+ and RADIUS support password encryption (TACACS+ encrypts all communication) and use Layer 4 protocol (TACACS+ uses TCP and RADIUS uses UDP). TACACS+ supports separation of authentication and authorization processes, while RADIUS combines authentication and authorization as one process. RADIUS supports remote access technology, such as 802.1x and SIP; TACACS+ does not."
    },
    {
        "id": 1039,
        "type": "radio",
        "question": "What function is provided by the RADIUS protocol?",
        "image": None,
        "options": [
            "RADIUS provides encryption of the complete packet during transfer.",
            "RADIUS provides separate AAA services.",
            "RADIUS provides separate ports for authorization and accounting.",
            "RADIUS provides secure communication using TCP port 49."
        ],
        "correct": [2],
        "explanation": "When an AAA user is authenticated, RADIUS uses UDP port 1645 or 1812 for authentication and UDP port 1646 or 1813 for accounting. TACACS provides separate authorization and accounting services. When a RADIUS client is authenticated, it is also authorized. TACACS provides secure connectivity using TCP port 49. RADIUS hides passwords during transmission and does not encrypt the complete packet."
    },
    {
        "id": 1040,
        "type": "checkbox",
        "question": "What are three characteristics of the RADIUS protocol? (Choose three.)",
        "image": None,
        "options": [
            "utilizes TCP port 49",
            "uses UDP ports for authentication and accounting",
            "supports 802.1X and SIP",
            "separates the authentication and authorization processes",
            "encrypts the entire body of the packet",
            "is an open RFC standard AAA protocol"
        ],
        "correct": [1, 2, 5],
        "explanation": "RADIUS is an open-standard AAA protocol using UDP port 1645 or 1812 for authentication and UDP port 1646 or 1813 for accounting. It combines authentication and authorization into one process; thus, a password is encrypted for transmission while the rest of the packet will be sent in plain text. RADIUS offers the expedited service and more comprehensive accounting desired by remote-access providers but provides lower security and less potential for customization than TACACS+."
    },
    {
        "id": 1041,
        "type": "radio",
        "question": "Which zone-based policy firewall zone is system-defined and applies to traffic destined for the router or originating from the router?",
        "image": None,
        "options": [
            "local zone",
            "inside zone",
            "self zone",
            "system zone",
            "outside zone"
        ],
        "correct": [2],
        "explanation": "Zone-based policy firewalls typically have the private (internal or trusted) zone, the public (external or untrusted) zone, and the default self zone, which does not require any interfaces. The private or internal zone is commonly used for internal LANs. The public zone would include the interfaces that connect to an external (outside the business) interface."
    },
    {
        "id": 1042,
        "type": "checkbox",
        "question": "What are two benefits of using a ZPF rather than a Classic Firewall? (Choose two.)",
        "image": None,
        "options": [
            "ZPF allows interfaces to be placed into zones for IP inspection.",
            "The ZPF is not dependent on ACLs.",
            "Multiple inspection actions are used with ZPF.",
            "ZPF policies are easy to read and troubleshoot.",
            "With ZPF, the router will allow packets unless they are explicitly blocked."
        ],
        "correct": [1, 3],
        "explanation": "There are several benefits of a ZPF:\n- It is not dependent on ACLs.\n- The router security posture is to block unless explicitly allowed.\n- Policies are easy to read and troubleshoot with C3PL.\n- One policy affects any given traffic, instead of needing multiple ACLs and inspection actions.\n\nIn addition, an interface cannot be simultaneously configured as a security zone member and for IP inspection."
    },
    {
        "id": 1043,
        "type": "matching",
        "question": "Place the steps for configuring zone-based policy (ZPF) firewalls in order from first to last. (Not all options are used.)",
        "image": None,
        "left_items": [
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th"
        ],
        "right_items": [
            "Apply policies.",
            "Assign zones to interfaces.",
            "Create access lists.",
            "Create policies.",
            "Create zones.",
            "Define traffic classes."
        ],
        "correct": [4, 5, 3, 0, 1],
        "explanation": "The correct order for configuring ZPF firewalls is:\n1st - Create zones.\n2nd - Define traffic classes.\n3rd - Create policies.\n4th - Apply policies.\n5th - Assign zones to interfaces.\n\n'Create access lists' is not used in this process."
    },
    {
        "id": 1044,
        "type": "radio",
        "question": "How does a firewall handle traffic when it is originating from the private network and traveling to the DMZ network? (SOSPECHOSA)",
        "image": None,
        "options": [
            "The traffic is selectively denied based on service requirements.",
            "The traffic is usually permitted with little or no restrictions.",
            "The traffic is selectively permitted and inspected.",
            "The traffic is usually blocked."
        ],
        "correct": [1],
        "explanation": "Traffic originating from the private network is inspected as it travels toward the public or DMZ network. This traffic is permitted with little or no restriction. Inspected traffic returning from the DMZ or public network to the private network is permitted.(TAMBIÉN PUEDE SER LA OPCIÓN 3: The traffic is selectively permitted and inspected.)"
    },
]