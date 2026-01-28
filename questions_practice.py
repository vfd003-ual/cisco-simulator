# Banco de preguntas Cisco Network Security - PRÁCTICA

questions_practice = [
    {
        "id": 1,
        "type": "checkbox",
        "question": "Which two statements are true about ASA standard ACLs? (Choose two.)",
        "options": [
            "They identify only the destination IP address",
            "They are the most common type of ACL",
            "They are applied to interfaces to control traffic",
            "They specify both the source and destination MAC address",
            "They are typically only used for OSPF routes"
        ],
        "correct": [0, 4],
        "explanation": "ASA standard ACLs are used to identify the destination IP addresses, unlike IOS ACLs where a standard ACL identifies the source host/network. They are typically only used for OSPF routes and can be used in a route map for OSPF redistribution. Standard access lists cannot be applied to interfaces to control traffic."
    },
    {
        "id": 2,
        "type": "checkbox",
        "question": "When dynamic NAT on an ASA is being configured, what two parameters must be specified by network objects? (Choose two.)",
        "options": [
            "the inside NAT interface",
            "the interface security level",
            "the outside NAT interface",
            "a range of private addresses that will be translated",
            "the pool of public global addresses"
        ],
        "correct": [3, 4],
        "explanation": "On an ASA, both the pool of addresses that will be used as inside global address and the range of internal private addresses that should be translated are configured through network objects."
    },
    {
        "id": 3,
        "type": "radio",
        "question": "Which protocol uses X.509 certificates to support mail protection performed by mail agents?",
        "options": [
            "IPsec",
            "SSL",
            "S/MIME",
            "EAP-TLS"
        ],
        "correct": [2],
        "explanation": "Many applications use the X.509 standard format of digital certificates to authenticate websites, public key distribution, and end devices connected to switch ports. User email agents use the S/MIME protocol to support email protection. S/MIME uses X.509 certificates."
    },
    {
        "id": 4,
        "type": "checkbox",
        "question": "What are two security features commonly found in a WAN design? (Choose two.)",
        "options": [
            "WPA2 for data encryption of all data between sites",
            "firewalls protecting the main and remote sites",
            "outside perimeter security including continuous video surveillance",
            "port security on all user-facing ports",
            "VPNs used by mobile workers between sites"
        ],
        "correct": [1, 4],
        "explanation": "WANs span a wide area and commonly have connections from a main site to remote sites including a branch office, regional site, SOHO sites, and mobile workers. WANs typically connect over a public internet connection. Each site commonly has a firewall and VPNs used by remote workers between sites."
    },
    {
        "id": 5,
        "type": "radio",
        "question": "What is an appropriate use for class 5 digital certificates?",
        "options": [
            "used for online business transactions between companies",
            "used for private organizations or government security",
            "used by organizations for which proof of identity is required",
            "used for testing in situations in which no checks have been performed"
        ],
        "correct": [1],
        "explanation": "The CA class number determines how rigorous the procedure was that verified the identity of the holder when the certificate was issued. The higher the class number, the more trusted the certificate. Class numbers range from 0 to 5. A class 5 certificate is the most trusted, and class 0 the least trusted. Class 5 is used for private organizations or government security."
    },
    {
        "id": 6,
        "type": "checkbox",
        "question": "Which two statements are characteristics of a virus? (Choose two.)",
        "options": [
            "A virus typically requires end-user activation",
            "A virus has an enabling vulnerability, a propagation mechanism, and a payload",
            "A virus replicates itself by independently exploiting vulnerabilities in networks",
            "A virus provides the attacker with sensitive data, such as passwords",
            "A virus can be dormant and then activate at a specific time or date"
        ],
        "correct": [0, 4],
        "explanation": "The type of end user interaction required to launch a virus is typically opening an application, opening a web page, or powering on the computer. Once activated, a virus may infect other files located on the computer or other computers on the same network."
    },
    {
        "id": 7,
        "type": "matching",
        "question": "Match the information security component with the description.",
        "left_items": ["Availability", "Confidentiality", "Integrity"],
        "right_items": [
            "Authorized users must have uninterrupted access to important resources and data",
            "Only authorized individuals, entities, or processes can access sensitive information",
            "Data is protected from unauthorized alteration"
        ],
        "correct": [0, 1, 2],
        "explanation": "Availability ensures authorized users have uninterrupted access, Confidentiality restricts access to authorized individuals only, and Integrity protects data from unauthorized changes."
    },
    {
        "id": 8,
        "type": "matching",
        "question": "Match the security policy with the description.",
        "left_items": [
            "acceptable use policy (AUP)",
            "remote access policy",
            "identification and authentication policy",
            "network maintenance policy"
        ],
        "right_items": [
            "identifies network applications and uses that are acceptable to the organization",
            "identifies how remote users can access a network and what is accessible via remote connectivity",
            "specifies authorized persons that can have access to network resources and identity verification procedures",
            "specifies network device operating systems and end user application update procedures"
        ],
        "correct": [0, 1, 2, 3],
        "explanation": "Each security policy defines specific guidelines: AUP for acceptable uses, remote access policy for remote connections, identification and authentication policy for access control, and network maintenance policy for system updates."
    },
    {
        "id": 9,
        "type": "radio",
        "question": "How does the service password-encryption command enhance password security on Cisco routers and switches?",
        "options": [
            "It encrypts passwords as they are sent across the network",
            "It encrypts passwords that are stored in router or switch configuration files",
            "It requires that a user type encrypted passwords to gain console access to a router or switch",
            "It requires encrypted passwords to be used when connecting remotely to a router or switch with Telnet"
        ],
        "correct": [1],
        "explanation": "The service password-encryption command encrypts plaintext passwords in the configuration file so that they cannot be viewed by unauthorized users."
    },
    {
        "id": 10,
        "type": "radio",
        "question": "Which benefit does SSH offer over Telnet for remotely managing a router?",
        "options": [
            "encryption",
            "TCP usage",
            "authorization",
            "connections via multiple VTY lines"
        ],
        "correct": [0],
        "explanation": "SSH provides secure access to a network device for remote management. It uses a stronger password authorization than Telnet does and encrypts any data that is transported during the session."
    },
    {
        "id": 11,
        "type": "radio",
        "question": "Refer to the exhibit. Which statement about the JR-Admin account is true?",
        "image": "/static/images/11.png",
        "options": [
            "JR-Admin can issue show, ping, and reload commands",
            "JR-Admin can issue ping and reload commands",
            "JR-Admin can issue only ping commands",
            "JR-Admin can issue debug and reload commands",
            "JR-Admin cannot issue any command because the privilege level does not match one of those defined"
        ],
        "correct": [1],
        "explanation": "Based on the privilege levels defined, the JR-Admin account with its assigned privilege level can execute ping and reload commands."
    },
    {
        "id": 12,
        "type": "radio",
        "question": "What protocol is used by SCP for secure transport?",
        "options": [
            "IPSec",
            "HTTPS",
            "SSH",
            "Telnet",
            "TFTP"
        ],
        "correct": [2],
        "explanation": "The Secure Copy (SCP) feature provides a secure and authenticated method for copying and saving router configuration files by using SSH."
    },
    {
        "id": 13,
        "type": "radio",
        "question": "Refer to the exhibit. What type of syslog message is displayed?",
        "image": "/static/images/13.png",
        "options": [
            "warning",
            "notification",
            "informational",
            "debugging"
        ],
        "correct": [1],
        "explanation": "The severity level is used to provide an explanation for the event or error that is occurring within the Cisco IOS. The smaller the number of the severity level, the more critical the event. A Syslog message with a level 5 is considered a notification message."
    },
    {
        "id": 14,
        "type": "radio",
        "question": "What command must be issued on a Cisco router that will serve as an authoritative NTP server?",
        "options": [
            "ntp master 1",
            "ntp server 172.16.0.1",
            "ntp broadcast client",
            "clock set 11:00:00 DEC 20 2010"
        ],
        "correct": [0],
        "explanation": "Routers that will serve as NTP masters must be configured with the ntp master command. A client is configured with the ntp server command so that the client can locate the NTP master. The ntp broadcast client command allows NTP to use to broadcast messages. The clock set command is used to set the time on a router."
    },
    {
        "id": 15,
        "type": "radio",
        "question": "A server log includes this entry: User student accessed host server ABC using Telnet yesterday for 10 minutes. What type of log entry is this?",
        "options": [
            "authentication",
            "authorization",
            "accounting",
            "accessing"
        ],
        "correct": [2],
        "explanation": "Accounting records what users do and when they do it, including what is accessed, the amount of time the resource is accessed, and any changes that were made. Accounting keeps track of how network resources are used."
    },
    {
        "id": 16,
        "type": "checkbox",
        "question": "Which three types of views are available when configuring the role-based CLI access feature? (Choose three.)",
        "options": [
            "superuser view",
            "root view",
            "superview",
            "CLI view",
            "admin view",
            "config view"
        ],
        "correct": [1, 2, 3],
        "explanation": "There are three types of Role-based CLI views: 1) root view, 2) CLI view, 3) superview"
    },
    {
        "id": 17,
        "type": "radio",
        "question": "What is the purpose of using the ip ospf message-digest-key key md5 password command and the area area-id authentication message-digest command on a router?",
        "options": [
            "to encrypt OSPF routing updates",
            "to enable OSPF MD5 authentication on a per-interface basis",
            "to configure OSPF MD5 authentication globally on the router",
            "to facilitate the establishment of neighbor adjacencies"
        ],
        "correct": [2],
        "explanation": "To configure OSPF MD5 authentication globally, the ip ospf message-digest-key key md5 password interface configuration command and the area area-id authentication message-digest router configuration command are issued. To configure OSPF MD5 authentication per interface, the ip ospf message-digest-key key md5 password interface configuration command and the ip ospf authentication message-digest interface configuration command are issued. Authentication does not encrypt OSPF routing updates. The requirements to establish OSPF router neighbor adjacencies are separate from authentication."
    },
    {
        "id": 18,
        "type": "radio",
        "question": "What is indicated by the use of the local-case keyword in a local AAA authentication configuration command sequence?",
        "options": [
            "that user access is limited to vty terminal lines",
            "that passwords and usernames are case-sensitive",
            "that AAA is enabled globally on the router",
            "that a default local database AAA authentication is applied to all lines"
        ],
        "correct": [1],
        "explanation": "The use of the local-case keyword means that the authentication is case-sensitive. It does not enable or apply the AAA configuration to router interfaces or lines."
    },
    {
        "id": 19,
        "type": "checkbox",
        "question": "A network administrator is configuring an AAA server to manage RADIUS authentication. Which two features are included in RADIUS authentication? (Choose two.)",
        "options": [
            "encryption for all communication",
            "hidden passwords during transmission",
            "single process for authentication and authorization",
            "separate processes for authentication and authorization",
            "encryption for only the data"
        ],
        "correct": [1, 2],
        "explanation": "RADIUS authentication supports the following features: RADIUS authentication and authorization as one process, encrypts only the password, utilizes UDP, and supports remote-access technologies, 802.1X, and Session Initiation Protocol (SIP)."
    },
    {
        "id": 20,
        "type": "radio",
        "question": "A network administrator is explaining to a junior colleague the use of the lt and gt keywords when filtering packets using an extended ACL. Where would the lt or gt keywords be used?",
        "options": [
            "in an IPv6 extended ACL that stops packets going to one specific destination VLAN",
            "in an IPv4 named standard ACL that has specific UDP protocols that are allowed to be used on a specific server",
            "in an IPv6 named ACL that permits FTP traffic from one particular LAN getting to another LAN",
            "in an IPv4 extended ACL that allows packets from a range of TCP ports destined for a specific network device"
        ],
        "correct": [3],
        "explanation": "The lt and gt keywords are used for defining a range of port numbers that are less than a particular port number or greater than a particular port number."
    },
    {
        "id": 21,
        "type": "radio",
        "question": "Which feature is unique to IPv6 ACLs when compared to those of IPv4 ACLs?",
        "options": [
            "the use of wildcard masks",
            "an implicit deny any any statement",
            "the use of named ACL statements",
            "an implicit permit of neighbor discovery packets"
        ],
        "correct": [3],
        "explanation": "One of the major differences between IPv6 and IPv4 ACLs are two implicit permit statements at the end of any IPv6 ACL. These two permit statements allow neighbor discovery operations to function on the router interface."
    },
    {
        "id": 22,
        "type": "radio",
        "question": "Refer to the exhibit. An extended access list has been created to prevent human resource users from gaining access to the accounting server. All other network traffic is to be permitted. When following the ACL configuration guidelines, on which router, interface, and direction should the access list be applied?",
        "image": "/static/images/22.png",
        "options": [
            "router R1, interface S0/1/0, outbound",
            "router R2, interface Gi0/0/1, outbound",
            "router R2, interface Gi0/0/1, inbound",
            "router R1, interface Gi0/0/0, inbound",
            "router R2, interface S0/1/1, inbound",
            "router R1, interface Gi0/0/0, outbound"
        ],
        "correct": [3],
        "explanation": "The ACL configuration guidelines recommend placing extended access control lists as close to the source of network traffic as possible and placing standard access control lists as close to the destination of network traffic as possible."
    },
    {
        "id": 23,
        "type": "radio",
        "question": "Which statement describes the characteristics of packet-filtering and stateful firewalls as they relate to the OSI model?",
        "options": [
            "Both stateful and packet-filtering firewalls can filter at the application layer",
            "A stateful firewall can filter application layer information, whereas a packet-filtering firewall cannot filter beyond the network layer",
            "A packet-filtering firewall typically can filter up to the transport layer, whereas a stateful firewall can filter up to the session layer",
            "A packet-filtering firewall uses session layer information to track the state of a connection, whereas a stateful firewall uses application layer information to track the state of a connection"
        ],
        "correct": [2],
        "explanation": "Packet filtering firewalls can always filter Layer 3 content and sometimes TCP and UDP-based content. Stateful firewalls monitor connections and thus have to be able to support up to the session layer of the OSI model."
    },
    {
        "id": 24,
        "type": "radio",
        "question": "Which special hardware module, when integrated into ASA, provides advanced IPS features?",
        "options": [
            "Content Security and Control (CSC)",
            "Advanced Inspection and Prevention (AIP)",
            "Advanced Inspection and Prevention Security Services Card (AIP-SSC)",
            "Advanced Inspection and Prevention Security Services Module (AIP-SSM)"
        ],
        "correct": [1],
        "explanation": "The advanced threat control and containment services of an ASA firewall are provided by integrating special hardware modules with the ASA architecture. These special modules include: Advanced Inspection and Prevention (AIP) module – supports advanced IPS capability. Content Security and Control (CSC) module – supports antimalware capabilities. Cisco Advanced Inspection and Prevention Security Services Module (AIP-SSM) and Cisco Advanced Inspection and Prevention Security Services Card (AIP-SSC) – support protection against tens of thousands of known exploits."
    },
    {
        "id": 25,
        "type": "radio",
        "question": "Refer to the exhibit. A network administrator is configuring the security level for the ASA. What is a best practice for assigning the security level on the three interfaces?",
        "image": "/static/images/25.png",
        "options": [
            "Outside 0, Inside 35, DMZ 90",
            "Outside 40, Inside 100, DMZ 0",
            "Outside 0, Inside 100, DMZ 50",
            "Outside 100, Inside 10, DMZ 40"
        ],
        "correct": [2],
        "explanation": "The Cisco ASA assigns security levels to distinguish among different networks it connects. Security levels define the level of trustworthiness of an interface. The higher the level, the more trusted the interface. The security level numbers range between 0 (untrustworthy) to 100 (very trustworthy). Therefore, the interface connecting to the Internet should be assigned the lowest level. The interface connecting to the internal network should be assigned the highest level. The interface connecting to the DMZ network should be assigned a level between them."
    },
    {
        "id": 26,
        "type": "radio",
        "question": "What is an advantage in using a packet filtering firewall versus a high-end firewall appliance?",
        "options": [
            "Packet filters perform almost all the tasks of a high-end firewall at a fraction of the cost",
            "Packet filters represent a complete firewall solution",
            "Packet filters are not susceptible to IP spoofing",
            "Packet filters provide an initial degree of security at the data-link and network layer"
        ],
        "correct": [0],
        "explanation": "There are several advantages of using a packet filtering firewall: allows for implementing simple permit or deny rule sets, has a low impact on network performance, is easy to implement and is supported by most routers, provides an initial degree of security at the network layer, and performs almost all the tasks of a high-end firewall at a much lower cost."
    },
    {
        "id": 27,
        "type": "radio",
        "question": "Which type of firewall is commonly part of a router firewall and allows or blocks traffic based on Layer 3 and Layer 4 information?",
        "options": [
            "stateless firewall",
            "stateful firewall",
            "proxy firewall",
            "application gateway firewall"
        ],
        "correct": [0],
        "explanation": "A stateless firewall uses a simple policy table look-up that filters traffic based on specific criteria. These firewalls are usually part of a router firewall. They permit or deny traffic based on Layer 3 and Layer 4 information."
    },
    {
        "id": 28,
        "type": "radio",
        "question": "A company is deploying a new network design in which the border router has three interfaces. Interface Serial0/0/0 connects to the ISP, GigabitEthernet0/0 connects to the DMZ, and GigabitEthernet/01 connects to the internal private network. Which type of traffic would receive the least amount of inspection (have the most freedom of travel)?",
        "options": [
            "traffic that is going from the private network to the DMZ",
            "traffic that originates from the public network and that is destined for the DMZ",
            "traffic that is returning from the DMZ after originating from the private network",
            "traffic that is returning from the public network after originating from the private network"
        ],
        "correct": [0],
        "explanation": "Most traffic within an organization originates from a private IP address. The amount of inspection done to that traffic depends on its destination or whether traffic that is going to that private IP address originated the connection. The demilitarized zone typically holds servers. Traffic that is destined to those servers is filtered based on what services are being provided by the server (HTTP, HTTPS, DNS, etc.)."
    },
    {
        "id": 29,
        "type": "checkbox",
        "question": "What are two benefits offered by a zone-based policy firewall on a Cisco router? (Choose two.)",
        "options": [
            "Policies are defined exclusively with ACLs",
            "Policies are applied to unidirectional traffic between zones",
            "Policies provide scalability because they are easy to read and troubleshoot",
            "Any interface can be configured with both a ZPF and an IOS Classic Firewall",
            "Virtual and physical interfaces are put in different zones to enhance security"
        ],
        "correct": [1, 2],
        "explanation": "There are several benefits of a ZPF: It is not dependent on ACLs. The router security posture is to block unless explicitly allowed. Policies are easy to read and troubleshoot. This provides scalability because one policy affects any given traffic, instead of needing multiple ACLs and inspection actions for different types of traffic. Virtual and physical interfaces can be grouped into zones. Policies are applied to unidirectional traffic between zones. Both IOS Classic Firewalls and ZPFs can be enabled concurrently on a Cisco router. However, the models cannot be combined on a single interface."
    },
    {
        "id": 30,
        "type": "radio",
        "question": "When a Cisco IOS Zone-Based Policy Firewall is being configured via CLI, which step must be taken after zones have been created?",
        "options": [
            "Design the physical infrastructure",
            "Establish policies between zones",
            "Identify subsets within zones",
            "Assign interfaces to zones"
        ],
        "correct": [1],
        "explanation": "The steps for configuring zones in a Zone-Based Policy Firewall are as follows: Step 1. Determine the zones. Step 2. Establish policies between zones. Step 3. Design the physical infrastructure. Step 4. Identify subsets within zones and merge traffic requirements."
    },
    {
        "id": 31,
        "type": "checkbox",
        "question": "What are two shared characteristics of the IDS and the IPS? (Choose two.)",
        "options": [
            "Both are deployed as sensors",
            "Both analyze copies of network traffic",
            "Both use signatures to detect malicious traffic",
            "Both have minimal impact on network performance",
            "Both rely on an additional network device to respond to malicious traffic"
        ],
        "correct": [0, 2],
        "explanation": "Both the IDS and the IPS are deployed as sensors and use signatures to detect malicious traffic. The IDS analyzes copies of network traffic, which results in minimal impact on network performance. The IDS also relies on an IPS to stop malicious traffic."
    },
    {
        "id": 32,
        "type": "checkbox",
        "question": "When a Cisco IOS Zone-Based Policy Firewall is being configured, which two actions can be applied to a traffic class? (Choose two.)",
        "options": [
            "log",
            "hold",
            "drop",
            "inspect",
            "copy",
            "forward"
        ],
        "correct": [2, 3],
        "explanation": "The three actions that can be applied are inspect, drop, and pass. Inspect – This action offers state-based traffic control. Drop – This is the default action for all traffic. Similar to the implicit deny any at the end of every ACL, there is an explicit drop applied by the IOS to the end of every policy map. Pass – This action allows the router to forward traffic from one zone to another."
    }
]