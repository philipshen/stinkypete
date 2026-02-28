# Strategic Analysis: Cybersecurity Beneficiaries in the Context of US-Iran Escalation (2026)

### Executive Summary

**Key Points:**
*   **Geopolitical Context:** As of February 28, 2026, the commencement of "Operation Epic Fury" by US and Israeli forces against Iran has triggered a maximum-alert cyber threat environment. This follows the June 2025 "Midnight Hammer" strikes, marking a definitive shift from proxy conflict to direct military engagement [cite: 1, 2].
*   **Sector Impact:** The cybersecurity sector is experiencing a dual-force market dynamic: a surge in government and enterprise demand driven by Iranian retaliatory threats (wiper malware, critical infrastructure attacks), countered by valuation volatility stemming from AI disruption fears (e.g., Anthropic’s Claude Code Security release) [cite: 3, 4].
*   **Key Beneficiaries:** 
    *   **Palo Alto Networks (PANW):** Best positioned for government spending capture due to the GSA "OneGov" agreement and the strategic acquisition of CyberArk for identity security [cite: 5, 6].
    *   **CrowdStrike (CRWD):** Dominant in endpoint detection and response (EDR), crucial for countering Iranian wiper attacks, though facing short-term stock pressure from AI commoditization narratives [cite: 3, 7].
    *   **Zscaler (ZS):** Leverages "FedRAMP High" status and the Red Canary acquisition to secure federal networks and provide managed detection and response (MDR) [cite: 8, 9].
    *   **Fortinet (FTNT):** Critical for Operational Technology (OT) defense, specifically protecting industrial control systems (PLCs) targeted by groups like CyberAv3ngers [cite: 10, 11].

---

## 1. Comprehensive Analysis of Iran's APT Capabilities

Iran’s cyber strategy has evolved from simple website defacement to sophisticated espionage and destructive "wiper" attacks. In the context of the 2026 conflict, these capabilities represent a primary asymmetric weapon against superior US/Israel kinetic force.

### Major Advanced Persistent Threat (APT) Groups

**APT33 (Elfin / Peach Sandstorm / Refined Kitten)**
*   **Focus:** Aerospace, Energy, Petrochemical sectors.
*   **Capabilities:** Known for destructive malware, specifically the **Shamoon** wiper variants. APT33 has shifted from pure espionage to kinetic-style disruption, targeting industrial control systems (ICS) to inflict physical damage or operational paralysis [cite: 12, 13].
*   **Evolution:** In the 2025-2026 theater, APT33 has expanded operations to target satellite communications and critical infrastructure in US swing states, demonstrating intent to disrupt democratic processes and logistics [cite: 14].

**APT34 (OilRig / Helix Kitten / Hazel Sandstorm)**
*   **Focus:** Government, Financial, Telecommunications, Energy.
*   **Capabilities:** Specializes in supply chain attacks and sophisticated social engineering. They utilize custom backdoors (e.g., Karkoff, Shark) and DNS tunneling for command and control (C2) to evade detection [cite: 12].
*   **Tactics:** Recent campaigns have utilized compromised credentials linked to third-party vendors (e.g., Salesloft Drift) to breach downstream customers of major cybersecurity firms, highlighting their focus on supply chain leverage [cite: 15].

**APT35 (Charming Kitten / Magic Hound / Phosphorus)**
*   **Focus:** Human Intelligence (HUMINT), Dissidents, Israel/US Government officials, Academia.
*   **Capabilities:** Highly aggressive social engineering and "targeted phishing." Post-June 2025, this group escalated attempts to hack private accounts (Google, Telegram) of Israeli officials and researchers to gather intelligence for kinetic targeting [cite: 16].
*   **Evolution:** They have incorporated AI-enhanced social engineering to craft high-trust phishing lures, significantly increasing their success rate against high-value targets [cite: 17].

**MuddyWater (Seedworm / Static Kitten)**
*   **Focus:** Espionage and Disruption across the Middle East, Europe, and North America.
*   **Affiliation:** Subordinate to the Iranian Ministry of Intelligence and Security (MOIS) [cite: 12, 18].
*   **Tactics:** Known for "living off the land" (using legitimate tools like PowerShell) to avoid detection. In late 2025, they utilized compromised mailboxes via legitimate VPNs to distribute the Phoenix backdoor to over 100 government entities [cite: 19].

**CyberAv3ngers (IRGC-CEC)**
*   **Focus:** Operational Technology (OT) and Critical Infrastructure (Water, Energy).
*   **Significance:** affiliated with the Islamic Revolutionary Guard Corps Cyber-Electronic Command (IRGC-CEC). They gained notoriety for compromising Unitronics Programmable Logic Controllers (PLCs) in US water authorities (e.g., Aliquippa, PA) using default passwords to display anti-Israel messaging [cite: 10, 20].
*   **Escalation:** This group represents the most direct threat to US physical safety, targeting the OT/ICS layer where digital attacks cause physical consequences [cite: 21].

---

## 2. Historical Precedent for Cyber Escalation

Understanding Iran's retaliation patterns provides the roadmap for the 2026 "Operation Epic Fury" fallout.

**The Post-Soleimani Escalation (2020)**
Following the US assassination of Qassem Soleimani, Iranian cyber activity spiked. Hackers defaced government websites and probed US networks. However, the retaliation was somewhat restrained, focusing on "influence operations" and low-level disruption rather than catastrophic infrastructure attacks, likely to avoid provoking a full-scale war [cite: 22, 23].

**Saudi Aramco (2012) & Shamoon**
The benchmark for Iranian destructive capability is the 2012 attack on Saudi Aramco. Using the **Shamoon** wiper malware, Iranian actors destroyed data on 30,000 workstations, effectively forcing the world's largest oil company back to typewriters and fax machines for weeks. This demonstrated Iran's willingness to inflict massive economic damage on US allies [cite: 22, 24].

**Albanian Government Attacks (2022)**
Iran launched a destructive cyberattack against Albania (a NATO member) in retaliation for hosting the MEK (an Iranian dissident group). The attack destroyed government data and disrupted public services, leading to the severance of diplomatic ties. This proved Iran is willing to target sovereign government networks of US allies with destructive intent [cite: 14].

**Operation Midnight Hammer (June 2025)**
In the lead-up to the current conflict, the US/Israel "Midnight Hammer" operation against Iranian nuclear facilities triggered a wave of retaliatory DDoS and ransomware attacks against US financial institutions and infrastructure, serving as a prelude to the current full-scale cyber warfare [cite: 20, 25].

---

## 3. Expected Cyber Escalation Scenarios: 2026 Conflict

With "Operation Epic Fury" initiating major combat operations on February 28, 2026 [cite: 1], the following escalation scenarios are assessed as highly probable:

*   **Critical Infrastructure (Water/Energy):**
    *   **Scenario:** Simultaneous compromise of PLCs (e.g., Unitronics, Rockwell) in US water treatment and power distribution grids.
    *   **Actor:** CyberAv3ngers / APT33.
    *   **Impact:** Disruption of clean water supply or local power outages to induce panic. CISA has explicitly warned of this threat vector regarding OT devices [cite: 4, 26].

*   **Financial System Disruption:**
    *   **Scenario:** High-bandwidth Distributed Denial of Service (DDoS) attacks combined with "wiper" malware disguised as ransomware targeting US banks and trading platforms.
    *   **Actor:** APT34 / MuddyWater.
    *   **Precedent:** The 2012-2013 Operation Ababil against US banks [cite: 27].
    *   **2026 Context:** Iranian hacktivists have already targeted US financial entities following the June 2025 strikes [cite: 17].

*   **Defense Industrial Base (DIB) Espionage:**
    *   **Scenario:** Penetration of US defense contractors to exfiltrate logistics data, weapon schematics, or supply chain schedules to aid Iranian military defense.
    *   **Actor:** APT35 / MuddyWater.
    *   **Warning:** US agencies (FBI/CISA/NSA) issued a joint advisory warning DIB companies with ties to Israel are at "elevated risk" [cite: 28].

*   **Destructive "Wiper" Attacks:**
    *   **Scenario:** Deployment of malware designed solely to erase data (no ransom possibility) across US government and enterprise networks to impose economic costs.
    *   **Mechanism:** Exploitation of unpatched vulnerabilities (VPNs, Firewalls) to lateral movement [cite: 23, 29].

---

## 4. Analysis of Cybersecurity Beneficiaries

The threat landscape described above creates a specific demand profile: **Endpoint Protection** (to stop wipers), **Network Security** (to block command & control), **OT Security** (to protect infrastructure), and **Identity Security** (to prevent credential abuse).

### **Palo Alto Networks (PANW)**
*   **Strategic Positioning:** PANW is arguably the strongest beneficiary of government spending due to its "Platformization" strategy.
*   **Government Spend:** In December 2025, PANW secured a massive **GSA "OneGov" agreement**, offering federal agencies up to 60% discounts to standardize on their AI, Cloud, and Zero Trust platforms. This establishes PANW as a primary vendor for the federal government's AI adoption and security modernization [cite: 5, 30].
*   **Technical Fit:** The acquisition of **CyberArk** ($25B deal completed Feb 2026) integrates privileged access management (PAM) into PANW's stack. This directly counters Iranian tactics which rely heavily on credential harvesting and privilege escalation (e.g., APT34, APT35) [cite: 6, 31].
*   **Iranian TTP Counter:** Their Cortex XSIAM platform addresses the need for automated SOC responses to high-volume Iranian attacks [cite: 32].

### **CrowdStrike (CRWD)**
*   **Strategic Positioning:** The premier player in Endpoint Detection and Response (EDR).
*   **Enterprise Surge:** The **Falcon Flex** subscription model has seen massive adoption (over $1.35B ARR from Flex accounts), allowing enterprises to rapidly deploy modules (like identity protection) in response to the heightened threat environment [cite: 7, 33].
*   **Technical Fit:** CrowdStrike’s single-agent architecture is critical for detecting "living off the land" attacks (used by MuddyWater) and preventing the execution of wiper malware (Shamoon variants). Their "OverWatch" threat hunting team provides human intelligence to counter Iranian APTs [cite: 34].
*   **Government:** Strong presence in the Defense Industrial Base (DIB) and widely used by federal agencies for EDR/XDR [cite: 35].

### **Zscaler (ZS)**
*   **Strategic Positioning:** Leader in Zero Trust Architecture (ZTA), replacing legacy VPNs which are frequent targets of Iranian exploitation [cite: 18].
*   **Government Spend:** Zscaler Internet Access (ZIA) and Private Access (ZPA) have achieved **FedRAMP High** authorization, making them the default choice for high-security federal agencies and the DoD. They are positioned to capture the "multi-billion dollar shift to Zero Trust" mandated by the US government [cite: 9, 36].
*   **SecOps Expansion:** The acquisition of **Red Canary** ($675M) adds Managed Detection and Response (MDR) capabilities, allowing Zscaler to not just secure the pipe, but manage the threat response—a key requirement for agencies lacking internal SOC manpower [cite: 8, 37].

### **Fortinet (FTNT)**
*   **Strategic Positioning:** Leader in firewall/network security with a specific advantage in Operational Technology (OT).
*   **OT/ICS Defense:** With Iranian groups like CyberAv3ngers targeting Unitronics PLCs and other industrial gear, Fortinet’s specialized OT security solutions and ruggedized firewalls are essential for protecting water, energy, and manufacturing sectors [cite: 10, 11].
*   **Financial Strength:** Fortinet reported strong Q4 2025 results with a hardware refresh cycle contributing to 20% product revenue growth. This hardware is often the first line of defense for critical infrastructure [cite: 38, 39].

---

## 5. Revenue Exposure & Competitive Advantages

| Company | Revenue / Financials (Recent) | Government Contract Position | Competitive Advantage |
| :--- | :--- | :--- | :--- |
| **Palo Alto Networks (PANW)** | Q4 FY2025 Rev: $2.5B (+16% YoY). NGS ARR: $5.6B [cite: 40]. | **GSA "OneGov" Agreement:** 60% discount vehicle to lock in federal agencies through 2028 [cite: 5]. | **Platformization:** Integrating Network, Cloud, SOC, and Identity (via CyberArk) into a single vendor stack. |
| **CrowdStrike (CRWD)** | Q3 FY2026 Rev: $1.23B (+22% YoY). ARR: $4.92B [cite: 33, 41]. | High penetration in Defense Industrial Base (DIB); "Falcon Flex" allows rapid procurement [cite: 7]. | **Endpoint Dominance:** Best-in-class efficacy against malware/wipers; rapid deployment during crises. |
| **Zscaler (ZS)** | Q2 FY2026 Rev: $816M (+26% YoY). Rule of 62 (Growth+Margin) [cite: 42]. | **FedRAMP High:** Essential for DoD/Intel community. Mandated Zero Trust architecture alignment [cite: 9]. | **Zero Trust Proxy:** Eliminates attack surface by hiding apps from the internet (anti-VPN exploitation). |
| **Fortinet (FTNT)** | Q4 2025 Rev: $1.91B (+15% YoY). Free Cash Flow: $2.21B [cite: 39]. | Strong in State/Local Govt & Utilities due to cost-efficiency and OT capabilities. | **OT/ICS Security:** proprietary ASICs provide high performance for industrial environments [cite: 43]. |

---

## 6. Historical Stock Performance During Crises

*   **Soleimani Strike (Jan 2020):** Following the strike, defense and cyber stocks spiked. CrowdStrike and Zscaler saw immediate interest as fears of retaliation grew, while traditional defense contractors (Raytheon, Lockheed) also jumped [cite: 44].
*   **Israel-Hamas War (Oct 2023):** Cyber stocks were mixed but resilient. Israeli-based firms like Check Point (CHKP) and CyberArk (CYBR) faced initial volatility due to operational location concerns but recovered quickly as the "war premium" (demand for their tech) outweighed operational risks [cite: 45, 46].
*   **2026 War Context:**
    *   **Post-Feb 2026 Escalation:** The "Operation Epic Fury" announcement is expected to act as a massive tailwind for the sector, similar to the 2022 Russia-Ukraine conflict which drove a surge in European defense spending.
    *   **The "Anthropic Dip" (Feb 2026):** Conversely, the sector suffered a sharp sell-off (~5-11%) in late February 2026 following the release of **Anthropic's "Claude Code Security"**, which investors feared would automate code patching and reduce demand for traditional cyber tools. CrowdStrike dropped ~10%, Zscaler ~10% [cite: 3, 47]. *Note: This creates a potential "buy the dip" opportunity where the war-driven demand reality conflicts with the AI-driven displacement fear.*

---

## 7. Risk Factors & Bear Cases

While the "War Thesis" is bullish, significant risks exist:

1.  **AI Commoditization (The Anthropic Threat):**
    *   **Risk:** Tools like "Claude Code Security" can scan code and fix vulnerabilities faster than human teams. Investors fear this will commoditize "shift-left" security and code scanning, hurting companies that rely on seat-based pricing for developers [cite: 3].
    *   **Counter-argument:** CrowdStrike CEO George Kurtz argues AI scanners do not replace *infrastructure* protection or runtime defense (EDR), which are necessary to stop active attacks [cite: 48].

2.  **Valuation Concerns:**
    *   **Risk:** CrowdStrike trades at ~103x forward earnings, and Zscaler at ~50x. These are priced for perfection. Any deceleration in growth, or "billings" misses (as seen with Fortinet in the past), can lead to rapid multiple compression [cite: 49, 50].

3.  **Vendor Breach Risk:**
    *   **Risk:** Iranian actors targeting the supply chain (e.g., the SolarWinds or Salesloft precedents) could compromise a major vendor. If PANW or ZS were breached to attack their customers, their stock would suffer catastrophic reputational damage [cite: 15].

4.  **Operational Disruption in Israel:**
    *   **Risk:** Palo Alto Networks (via CyberArk acquisition) and other firms have significant R&D in Israel. Physical conflict (missile strikes on Tel Aviv) could disrupt operations, though most have contingency plans [cite: 45, 51].

---

## 8. Conclusion & Open Questions

**Conclusion:**
The outbreak of direct conflict between the US/Israel and Iran ("Operation Epic Fury") creates a textbook "flight to safety" trade for the cybersecurity sector. The threat of destructive wipers (Shamoon), OT attacks (CyberAv3ngers), and massive espionage campaigns forces government and enterprise hands to increase spending.

**Palo Alto Networks** appears the most robustly positioned "anchor" holding due to its GSA government dominance and identity security consolidation. **CrowdStrike** offers the highest "beta" to the threat environment (endpoint protection is the first line of defense against wipers) but carries higher valuation risk. **Zscaler** is the pure-play on federal Zero Trust mandates.

**Open Questions for Further Investigation:**
1.  **CyberArk Integration:** How quickly can PANW integrate CyberArk's sales force to capitalize on the GSA OneGov vehicle? Disruption during integration is a risk [cite: 51].
2.  **Specific OT Targets:** Are there confirmed breaches of US water/energy utilities post-Feb 2026? Confirmation would spike FTNT and CRWD demand.
3.  **Anthropic Impact:** Will Q1 2026 earnings show any slowdown in "code security" module adoption due to AI tools, or was the market reaction purely sentiment-driven?
4.  **DIB Funding:** Has Congress passed emergency supplemental appropriations for the Defense Industrial Base cyber hardening that would directly fund these contracts?

---

### **Source References**

*   **[cite: 35]** MarketsandMarkets (Govt Cyber Market)
*   **[cite: 15]** Cybersecurity Dive (Supply Chain Attacks)
*   **[cite: 12]** Picus Security (Iranian APTs)
*   **[cite: 13]** Trellix (Iranian Cyber Capability)
*   **[cite: 52]** Nozomi Networks (CyberAv3ngers/OT)
*   **[cite: 22]** United Against Nuclear Iran (History of Attacks)
*   **[cite: 24]** Atlantic Council (Aramco Attack)
*   **[cite: 20]** Arctic Wolf (Escalation Risks)
*   **[cite: 53]** NSA/CISA Joint Advisory (Iran Targets US)
*   **[cite: 54]** Zscaler Investor Relations (Q2 2026 Financials)
*   **[cite: 55]** Fortinet Investor Relations (Q4 2025 Financials)
*   **[cite: 40]** Palo Alto Networks (Q4 2025 Financials)
*   **[cite: 44]** Washington Post (2020 Soleimani Stock Reaction)
*   **[cite: 1]** Atlantic Council (Operation Epic Fury)
*   **[cite: 4]** CISA Joint Fact Sheet (June 2025)
*   **[cite: 5]** GSA.gov (OneGov Agreement with PANW)
*   **[cite: 6]** CRN (PANW acquires CyberArk)
*   **[cite: 7]** MarketBeat (CrowdStrike Falcon Flex)
*   **[cite: 2]** Economic Times (Operation Epic Fury Details)
*   **[cite: 3]** Economic Times (Anthropic "Claude Code" Impact)
*   **[cite: 8]** Island.io (Zscaler acquires Red Canary)
*   **[cite: 10]** BankInfoSecurity (CyberAv3ngers Tactics)
*   **[cite: 9]** Chronicle Journal (Zscaler FedRAMP High)

**Sources:**
1. [atlanticcouncil.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIYyOG6TCrCGpwplofw1r1bwHArIpGXRN-l99dp4m9DZF5KJtIMQFUN6jZvw9ettmN4pLGNsIIvVlbick9r9sxwetzshil6ladXRkrSAcWpNvDbuTnw65WRlbcNdqNCW3Zexkeb5sg9pWsiGi-7Y4I3okSTw-3yk7qf8Nh33bdV6_OwUuWjxwp2C0DYpiJikvuU2wKJ6kfsiLJ7_BA_rJLU84tQRWYIKhq41qG-swQm6N6)
2. [economictimes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_4LM9mu6yOY2l8wuxkOmNU02Ua3nOHYoySUnvknW7sxMOSI3Hcc2EQ7ifZBVUcRZZ98Wklwigfi70wnnH-DrouBwNzHwjt-3tm1Q9LzdOqfgSFqv-D_As2iGCxS-CfhsuHjGjaINHOKPzr32cuw8ig8ddnyt40AvNm0BU0w3b5-sKaUCytN0bbg2fn0rmNahfTG5YNkCuebeDEc2r7GA126NTOJ3B0NsTjmqHAW-rCs9XL-uDqwd2okuKF5K0OdIDs0UCkfPQ-4iUrA7bNVZgHJL5U5zpgbIJkOajxl4AZRj5f_c-k3KxwgghRVHBncMn_Yl5-XvjQFRMRoVzLTha1l4e1kFzCHdDaRTeUMtMiH_WnJluThngz9jPm4Ntxe5yHWT3rO7YRVxA3RAd9j1foRNSDaVx6_bo_WccUjIfDvklxT8o3OGw5-PenZoFYnv4WSBP0enXB8_SuHEUmjTHdPeQnqQuioGaMO0517kD)
3. [economictimes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeWsFvive0su9XgQNwdoeu1h8U40KsrEkDF_2x-7v_R-va0A6VkNjGtQfPIXzxMZdpScN5Lk4_DdDAxT_G0CU8aNLSSDne5CvkA2dO-WTOMbEGRg7TMQh0-ZdM_G0B1GR7tRtRNQQJaSeIr44kuGiVWuAkn0FqrVGVGwWYzBnXxG92x8xtFxKCHgzneDMtNSpTRFoeg4Tan1fOiWi4a45Xt0adQXDYANSqCk7WisgpesSB2TMgVuazJsL7WoqPBQQSim24U9SjTP771MvIEZuBabbw1mCXZRqnGlaQRZEIEJ-4dM4Ygk-KQz9IFpzWhhK_Tg==)
4. [defense.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH25g4Dk__Hl16iCZJdELTqHVoybTJ84Jyo0VzMFKzZw4d4mo-YZah-BL1Q-j_J5A5dwiOwdRmQuUmFpJObPN-PQP5AO4ASKMv0Aj7ADldT2-pKfL2_wJDALCBq6IUOGflh9S2J6_4KFqC7nuuUOJb7O91bkFplQI4W7BtDzJZGE_9kbFDmEqk6hMBjcmzmbzmWNwvai5UqqncvCYks41BAmrQpANxpT0-xyGBtQN2pku_KBuPcujKMKmwgkYS3qKBBN3veCjsPiOoSbdskNtZfsvZzNGLzzEBK)
5. [gsa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqIX4BSaq5VW3qg1gWGm5m0rRSSygCN9hnfjYTSLo0kZB-d5blN1Jhc6p1mmCQlT4SfiP_pSG6JUR1fJAOrigqJvtA3CZiwBeJe1r3MpUc-dmE-yvAc3f_x53p67pjYV0ahtbw_71ARGTlbcZVLUWHs_943klUI5YEiEAF47SypyDge0mxdC3WLRIZIDXQ07V4mDNnVrr1S3ly4waxE-ZlDE_vTyS5zwwfQ8QPAKx9WZVEqWaL)
6. [crn.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2Vc4mZrfSx14NyEcNR3jPp_u2_4oWkGiPiY0lXSYaT-eKW5F0uhIVic94CzuMiZm3bHb3F9HDHmGoGSdFhzqeb5QUHE-z0wBqzIPUKIG4hGRgl_o2XohrPRDbFKzhAsAJxkV8thbfZ3gIrSwu1aGTAv88Fx8Qa1OS0ifdXJ2_lE__uJoK9qItPH3t8NGxXRufL5uv9sJ4LfaxjBNRW56_nf4kI8VPaURyGdv15JejkA==)
7. [tradingview.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFb-7OobENXzUaULk9q9vsjETUCaNSjg-5ojaitsFK1iQQnOEAMuSb66bPsGkaeyWIPfc7MRwaDHf4Acl1klejGuvRSBV2fNWZdzDKE1REKM5RjoPPPlmCAazREqLi3tKzg8IdrILU7gb_jvUyUV6MUtE0EQWmCcIfHP7RX67WYU3-A8MZzevwszgHFEaXorX88rEJK4rbb14GuDhJr8HGzdIjW8ZbffFMuGth9xzAVC6IXEg==)
8. [island.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFzSfjGBSv_GzWg3Twx0by0yqizXdC9qaeh7lb3VzcWUjNBa261QnJ1o7fPWGMhPe9lPxUyOfEiRk9YLaVPq4UUWY13Mkd7yjm6b8CXoAibLzJeT3iwgJB3MMW3rpvC92EFTN9qkTq2jLMI9hKte0eloYFuYmKl4HXJ8LrLD-XwrZRShxG9i8nAQ==)
9. [times-online.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECPEDnmWOpAgPlVl1JRJpTwsX7MK6i61SDRUfb3-fwKG3QWIM5vhutkklSJnFSu_FSJre1xX5i1BIjM5O8EcruPW1idyqVfNDCo73XOadvGlEy_adK1TmoFEvGxwj4sAe84bLUNAHecZztxiJ_ju3JAFgQzKQgEs78tzEoa0fhYnDDW0DgWKAHHy8s0Zyck-bL1UWh5UXq_EiSnSEH6IjYmzFk7SkBGgbVHP9yEzuZDPFhD9DUl0AbeuW1Yr3SCfg7sSj98z-tfkk=)
10. [bankinfosecurity.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0FIanpShNAJjK3XvV5sBa1VJlvOm0v2Fe71SoNtWAXuHKqkurfMhW4QT3ehNKnN7vmwnzGDXrumzlrDgPgYMiurj4mBdFfjJfn7Y7vD_HAxXGq6RD_HFUxTUbLrJd3K_xlCAmoi3OXS2aQxo4lqexlr4c)
11. [c2a-sec.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwisZ3OdIPHIPmjmKFxpX23r3E6pmTepQHV3ZgvtMEgd6VNA5eIt8KUcyvuwaRrTN-0m6dx00Lp2dO3WKuuGRlfzrJ5wEmXZD7pkGXLYyLpjw3biddbDQRl73QPiI1FtUtOtAbrg2Gx0oTObt15mFvCKVAKLemlb38vQqXgOBvIV4MV6DZujn8ZHNyWXaR-yIqnesdu3uiwBiadYBXK8e-st3oQ0Y42oT5OwU3Xi8RSA==)
12. [picussecurity.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_aca_Lw9kFkvd2CpJWLPuQPgxvTkAcxAAS3z3AetlGXWBWR1HHxONIl8tOidHa5s6-RtSNpnPFtknxW5UOgrXzQ9TffaaV-V_TKuBluavRmq9GynrcO4kOYLd1VoQp_y-5an_qCzmoN-w2GSGNmHvi2fpmvBUp-5jmLaoG3cNkMPOWIj3pgmqYA==)
13. [trellix.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoy1KAJ4Ol-mv2D9OSiOMN5dYcF47k5LeObWku2GNrJAUTKh5TbFXcPhhl6NBx3Y7cIO7oZSqeaw2vhKvB234sP2-QLUZpJ9DHJxMIDhuiLtr4aNfo6uLjKlGdOzCe5Ejeg6x_wBEhSuK16AYULywKcTgpr2oxV5-GeQ==)
14. [blumira.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU4p9igUAPJ0st-RzPQphJlZIbW5gdDY0g-7NlC5BQ0FxhesZQnMIVkfuVlD1my7U242q5MfPkJGsHEYVT7ZGyypHl4t031jfR10Ky-_pViPaDsD2G-q0kOGEy3brZj2HTIGZWPxBBv_1aCTy7opOOLQl5x00hOOBZcY07bXFJVckWSJnmqeGph-PvtZULjH2ldvA=)
15. [cybersecuritydive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEQw9eDn-5PUUtUp5uGaVx04KT3Ayth2TqDAwDdiWCDnyyqGF2-tgHNNxApqhebLAxNxijXVEDHuUbGtmNvbJNzIb_TjjCJI93bmkMbxlTIXrWQaHrMmabF5obkPPPBA37vmlGc79F8ZuOYzLq6C5hqB8NjuWioU9cclNh6pRve_skUCQFXAAoHpss9EfDdaQUr2LQ)
16. [timesofisrael.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkQxV9plFFQVtuQa0Zawe_zG4_qrpUD8QF6Auf4MakZ2jC6mwcnD0Edi9wnybTbHsD4Yl-utNJosLJa5wAMCd5EKlGPhOhhYI3iCS2Xd8WozDO4zXlZcp0TiOH1ZFKHW6nu-063ABsq1_qfkiIfWXKKZdHCe2zHsQOUFivVgUbI3k2zhAWD1LPtGfRjnOSErIvQBPRxFuNt89bX-38eLZuXg==)
17. [cyberproof.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmwhoLid-6fzQWsPV5q9TnJ646ZGW2EvH8aa7PO5rMyswF24PZxfLRhXkvhM3IRcXoCtLWr2o6vGOxwcxw_9pDqoTJK5awxeKzBII79rf5ij0DCDU9vsjm_Rr3d4JukF2fc2vDOo9SBhzbUjgpa3uFu7nppDFykj3P9127t_K-YLMCkR3yKZlF4yNhSaoUiFdh6g-EzCTY5i4=)
18. [cisa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBVn-r56XA4LVej6Rc5hhu2yvFrxqjQPADPzG8HT_hcjfgYGhAlm-zZLj-kJ5Uz96h2AwyZLJeh0opCTfsk0G6O8_Akxe-_Z94ApbowoLAArpnKaCvvTpncVWRLPvk8-oDyBkrPxN7Kaea42q7isBcdw-mCz_ETZvmSel662HVCuOX8mpa_GiJGpT8-Wj2p1ft5ccohk2--V55)
19. [group-ib.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5LqDPV1U8P96JjtxTe6LzU7O_kpOkpcZKs233VcbqxGCIIVPaEQpUJOp0yFPy-VWIzzuS5NcmxzO9CyUMtCotSU2klD6VH-dyDrRTL3rAQIvB9gZx5h3FQ0RSz7HxpL5-CKkcWrXvE1g=)
20. [arcticwolf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmPEWApYUjxsFZIcGqa1bQvFyjAUjFSQKNcFo7jXAya6SC9pJH-AVBj1rH4YoxO1yZhfQ32bJxV8lPpRKFYy90FiotUuFjqIL7wE-9CLFtf9UctqIodv5vUUum1fS505QODEuLBu5Nlr6W-ncFEqu2HoXJ0A6-qJl-se_A5TP8xrflxHiiQBiKsBtwFCyW)
21. [domaintools.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5Ay8Dh_mS5n6vZLgUtpD6A0FzbGVOJaZRvCJoqXfrH8vgguS9yHe0I_e7Q60nbVTZXJqLRMGtqEFOIINOmHbEHs7FZjV7hO2JDw1FV35X1nAb3YpIoJ7Sw7Up6mdAjXPd3t5EHV36XadebSzAwSy7NJDvciGJbU-k_gXbQ3H8yrQ2luM2PkHISx2iWXW9234Ev08u88xRjXKe-Chk8HGT6vX2r0N8v_Us813MGQ==)
22. [unitedagainstnucleariran.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqxWHreRwB4V06T6Hs6ChxEz8iykbmRF7yU0Ibc2ks96VICV5toKhLi6DT-nuswe6aYPQQu7t4jUpofYZIOCXCEdVy9iq5JxXxSI0sWPHf57gPOvwBiCFA5isMuVapOAXn8ycDTtWGZ_nZJl2l17aAdne-OmHuG_45WUmtSSIbDj5DoFH6grS3k07gc8s=)
23. [cyberscoop.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKU60x1__bfPGJlF3hyXKjoNfQ1NORxIzVsbNZOUk0XdxYkeo4nrBLHJd0NAcakrsb6czBLw_IzIxIRCpT4wBNu0_hZsKjwqT860FspNrR7MKyeASr9t8f2tnh3-y3XJT9SglrV-RSnn2rpU4Mlmv0JnZi0jg=)
24. [atlanticcouncil.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhXRUKJJawHg085cbyOHNKVKm3qYrIWHDQpp79vQIedrZrYq_bRomdz7QdI0DXB3HOOuPgCsWWXdmsgCvivzZoTY-wh2NJ-Q_KAXDd1p7yyeuliEPc3Htiv6tyq0jevk0dvPrB1e0Gdm9-C0NmPxI8neenvhWAiDYN0fOTUAdWS-EbYSfU9w19-RCOy0NVV3y7NzpQ_glNNyeD)
25. [aviationweek.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3W8EmBM81H4XnkVxsNqBYQf7nSdY4JODlDkRG1qu8JBks4p4fZYi67JvnIY1Krv3nwTyhIp7zVDHyHOBp5RQrsuzRNnOC1WQMHkcQbH6q_PWtO5yI489eu4gDfmneYoJ18Fs8lagfx5EahNnH7c_aRnY9VOVlIwyq6y52CSCyvqLvhnaioMxXtTpuVQ==)
26. [cisa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvRTb4NGIW8GdBDzvwMliDSfmI9CfmHWEMYvOQWDuTpICv1SLQFqyGNuQG7j9heEklLXeqfWri0C6HDE4pvITgx9PNs4QJMndsZ33IyAntLJfdIfEqeZKmQrXMbRjKPYukHOFQwAd_Aa2vFuqJqKPIS_SdQNmtzLr9bYRjamrmXU59IzwErSHLU2DgXmu2MoKDMLb7V4OFfGZD8_5z_-TX8zI6UWG3FgUDQGbl3WbGA3c=)
27. [timesofisrael.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIRs0WaAqAN0L-ZcB_bn4G0ALzPNu7WpV85fehzisO7OF-fBXa6DubmHERLvsq_bjXogaR08WzRqy3zOD43B5KcLYLmKbdgSyry9hncn3mEETXuo3PimxfANt_JIlLr1cJVOHOJbtZVw7QIPj0XcbqUlDqaEe36PELJK3iWsIAnffkK_vNCEb3Cu-Nwyqv)
28. [thehackernews.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWUVgr-V-IVdVBhizO9dhUoAqrONsbHqh2T8NwRVOgAaJDRtbZ36nLMa2srS5vGIM43mQPlZC7AOqecnbCgt65dtj-Rw3mgolTxDpAMaSNNuNj9M1nASstfcReV0yN8Z96B8TCwkkoi0MbD6iY2LzDN1O_xiTVyn-YNP_8XN52)
29. [paloaltonetworks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2IJdp6xK9a_bHSnvBfp6A5e2UsQsEwWobP1_WC8_kvSvFsRyLAUVmrzMLPbHblXUsfg4eoytN__iGlMwMufrKbqOfKWuJz77-HnrXNm0Iis4UPKs19GBs2BXO98F6yz4w-8M5fZd_NHpzQI6MNHEwyof-bA==)
30. [meritalk.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHf3meOwdpzltn9NAz_pcAGsxZIQxU5aJSvNfPAXs_LQfSv5U9eY89XMnnNOjT-JZc2teF4VUtO32O00IwxHx7Y1F_2NiwlMEo6BUhaxKehiTUzg_j3nyR2hiJmnZIyanTH6oa6Rqqg9ZdikNoTBEsRWWK1UEwzHEstQHYpmqWeOU9Jt2w=)
31. [paloaltonetworks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVwcJ33GVZQOzUTaMLDm7iqkvTt-C2ZUdrbUqCe60FzWrzv4wYms70FG1C_x-HKGi8AfVFgkDRIbBHaigos1_fMa-Vyi6skkrhEwGJWP4VsoKQVBMLvzIadu2102hd5hHg7JURFTztAvJrgaIxInKHCGbnmD4lucEK5sXHWTk3N2qP_IOQEjy0HThEouB0xmjTYSDgR69i5k1nMYjd60P2oe3ryyc_4jEvGKEwjhGdmtvxew==)
32. [futurumgroup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT9N58BY2Fm0Y3AgPC1MRX_foOt-Y7uTL1qnBq3RsNxGqf8DrmgTBl1NMFkZY_3SpPuSizwjTMexWR4YWoZIYZiPRazaLOJAfqThljQlVTTv2bU8Pk1i5BaMMF4-PYCERucDY4IQJUz9_SW54VI-CrXGT_65DSfAUNuOYN_WIkYbR-hNn9CfStI8cLj8NMZCInGdyXJp4pP8XN_NswVaqd7f4=)
33. [securitybrief.com.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDnq7x9vpQV47elGQ1M9N9M0HCDlRuaulGQcr7KFUzEXJN2mbLuF4Q6sXi2u4rmM2M6tyKAMPFX2lZXqNyXXCW3DNCKya8bf64VpExRZUHUAATSBrCm_b1CwjlS0bRliVY7yYGHw-PEe5MN6JukPZdu63Py4qCR1j4XA6Ok55r3yGG0_LP9MTJ3uvifbaZSvLxmxIg0f1YndizpA==)
34. [crowdstrike.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBqOJ8sv8MpUFxOWi3vQFOWLrWTFTGu8jx7fT-ypvoQBDa4Rer_iIhFYCxNa3DmU-prwYHLT-UZNXUTt23OXlhuo9W7uxDbYaMLc5SdHB4_pXQVavRMt6ILIt9QDADRSbGp3IsSyYhyQ2UCTXdP9GpJKKf1vLCdVq-aEmPqvJ7srUN)
35. [marketsandmarkets.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA8ST2QZQuuSXoANKcRaNs_Zj7iYGdt4eviEcZa1J-bY7a6QEGz4Quxh-1W3Qpx0iaE1zIa8ws7NV3mCORr2yKj5tx0d3doXPvX-yfCrBndYiv69ui5scKR3DABCHtT808h5LLNFhCpK6efVR1h5LYsPZQE2g3bmlxiRhML4biK7VTAzjzQVb_NFXcn7vlprBwQ7F-ocdDncEFwks=)
36. [zscaler.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDa46c_z4OqdBrH_Q3b1f5Qzf5QWydyGuXUfjs3ZDcZLAgkTU5j6d8OTmPuTj_rK5zl3o-RqeRPVmAGQVTQOVpChVthEmOhNsprm3KYgSK_zf85vOAUsyfxNEcP3o2vJZ0adjPh69R6VPHtFOnew==)
37. [zscaler.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3NO-oAR6fw1-p1NyFsWwCIFCystQwo94ropMQXG-9nwTfk46ZLOje1S2LZwSwT1csmBHK8SL7PeMliiCaXM7v20EjjRyUMztz6v2lekE9MzR28ALB2dmkyMoZqw0CnYJD9c6MDoRXsAe1R1f-X-fplTULfkivIVeGPT1a_b-0GhoVJNUmzs3NUuwjPgkp3yFA_AeDzvp1S4jcscgisu0eZn5NGqfnCaNVu4CkCfA=)
38. [fortinet.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFS2u0nKHd7963gXX6KH_SO4CWrQ0Jlg5tuxymhQm_5sihEU2TxYwLk6jCxyQAL-htNfk5oVJ61-4Nmt50a_gvleE03sLXeywi8QefY1M_EUx0JrVdDKoSVmrueZxg1FaBvwaBbgvzNhDIbpUbPErMWM8GiOGQFJpXqKlyafxoRCVI5hX_-)
39. [finviz.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbt8WXzD14mlLwe-iK0rWgbWpIWBi3wR0wg8Eukw1GkIKYuA1HwwbKY2SwWNn9HGNmtBq0O9gyHjOWeSv08NxUK8HDV_xqXVJs8n4YIPK9TMSwqKlHPKT4VPyMC21R8sHsm5oqK7LyfQpGsKGjFrQtYWWOo8-VbEO8iWjlH46EnSnnyGgn_Spf9ruGa7xB1XaWe0P2NMViOoTl3QXs3ZB3)
40. [paloaltonetworks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjOFw_xBoRriZQHtWJYt7sC0KF1Y-1y399jhIuSxjXodrBSyJlAWHNOMvBwvhZQcQWReQtp1U6quWeLwYRNSYUTavm0MVYUWOaQhvWC9dphlHLNqEW9E8yXBK3hiOZWdRloyfOERfn7q8G9UO-Uczty-TJC50u5T5vxjC32VIezEvx1e5TNDABSQ8OHnlNvgeK7M26ZOGIyV28WIM76mPGt8PyuP4PSaZkLhe27TYSuUTjHsdkNdERFUDuhUyRhCHegQ==)
41. [finviz.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEx8JLRYlS3KaFTq_0xdPC43NMTwLtogwWnhTBxCVziHcxZ93ijn4P_lCefpPSaoMM1XaUAVD14IxJjp4jO_NXl-HB1YyYySeiUlk3ktRWesNWOIS_-scy8RqEpNkdgLgKbfswVP1Cv5XaxSy2egMjnLYgHmeEaGDZwvZSmlPaYt7xWhO6vlHAY)
42. [investing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuF4EmzgELSUbqMfAqZvoCu3k69sBqLmZt7VQl8Zyq0vykY4M8cYLPstTM2z_vLleSeJF4PgkhuVbIsKTnPzZL3_e45uWrcXEXmxLXutvwe_j0TyGQlPFmQrElUh_UaVlloDqPQ4toF2OguvoQ0XhsAlNun_Kl1skmQ_BvJWsqTIvfXBErt2y7NsTDEOmibdXjFWpYyxEw9EGxdgeL6y7fkwgwUJZ9j36VGEfvF-OG9Cz4ypRhHhc=)
43. [fool.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQvtAuNJ7gb3F0Rca31AWX2AbcuSJX98RunA44-M9yj4D2ygH9rtpaPJ6f0pg0rV_PMM-_jiDn4oCoA_Hp-GJ0Q62RYN4PyAwcFbkqw-LPzRAVGh-3IaO2N0PcM49ai2Ggv6GJZpN59XJYGDvxn6KivKtrlNuas8WVuD7_XV0obsIvT4NDOa0awjlf1sJEp9G1SKc9BZ1-jFsAsvmEAJw=)
44. [washingtonpost.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGygbbBXTcqsNp-gzFyKYjeuiB2gKohfmiwmqvo-cVypktb-tA6MbJMKedesMf0lgd9eJzdY28h3hDPs83V-nmvGaNd1Hnp5Og5GZx3fR3Q2rHUonjB3XAlOt55qXLt3T15HdBtvPKH0uMBzbam5hWgiO1F2JKeN7Qdn6gVzwcv1treKctC6Y8AsG8DgNwPMk8k2WbuMmhGTPsJeBQv0ZQ4xVJ0kIDU3kkCJ8Wk)
45. [seekingalpha.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Kq-Kd12D5ZnquyRjFogQZCOJ4xZGgbYUp1njQSs3D1Udd79HDwCXG2s-7ZEfMXXazPtkgVO-H64BOq74jpb0YmNxnDq8RePfBar_ldMSlv5CEANsLtN1RwyXFyrs_Y-OvBcYrQoWds9oBN1I5-gG3rCXRuSsz0Gydg0oggC8IDU=)
46. [calcalistech.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpC_DVF8kGCZ0yiu2mJAV2AlUMtCaUoiB0l1rQEqMkepDtGhpoXBGUx8HIsMqwOk7GTI0wzRmApRGk9SkbGxpBGoquU7LU_OmNb6GkQ9nXbYpvb987u6DqCmwTcDvK2v5nDGhkQpvphkAIN2ylXg==)
47. [alphaspread.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4PFsLP-4WUCom-mJaNnJE1RBGPsduaVCvITPPJS54UTjxRjKflNcZPfn4Mqw7tu_RMOYCVdPSWBRMe60ogDyNOjU_TG4HEQN-MwBQdcjSntyloUaMzC8GhAeLFRkPW3Hil5Kd_gR4xBMoQIKiFcQo3RGuw2WaFT10Eh3_GG6hFszGo4GjH6NQGhjj3hLzkbt-QgGxrSrpaWA2PbyFCA7mkpJIAnkyu3zWGgu0kFyp00Ko5ueO)
48. [aimagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpPV_9_bCLbXy6RVqPTFG9iQJJaT0hSVySMhLbFU6nGo_USHpZhMoUWtR-i8A8vo6PFCZNksKI2u6V_wCA5QZgP6jaKPjn6ZNQLUvo9OH_N0wW4ilgH8tiBZf7x3WLAvb8TuiZkkYbMt4kSObh3bTsePnADNSGFJvF0WT4fO_NgT2GfZvdU4nLz1A=)
49. [247wallst.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFS7FtW7SxNJQ2HWjmGXAGx3MmlLrF2VrnfB2Rjd1RyLNjwmLCU3n0HirvsodBDWxAKINomBISq1shGS8cVc55BJUnAvWWq0xwsEr66lXYUhHGTUWwJQQJzAZvHQv6EGo5jvfETGqnmy2L9I0ECpA4nLl9hLWAcWo3KrZ9YWTsQ4_AWhRwcgb4rnEveb0RXdQrmgLTYquGCS7LfNXWkbjlnOh9rkBiwYlS65qfagWZNjOPr9w==)
50. [barchart.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjMTnYZT6DSZce9aAj9FYGxzrrcxnvgSqxC6aDcIBvFvZfTkhKcoTb3QSaPNTh0kzrq1I7gq4rX_vNfMg20gX3WwhOAQNMjaI9itUU0BUYHPQWJ6ImZ4Bw5r9boc_nSkpU0xV0xuNbRQU6QunTqYERu9iqUzcSpbJZL9InW3o6eTTUWJJ6ewHemgnHteLDWVHjKZsiHyaj37Cs3DUWbUlRWXPsS9xUB-QOmRiZXnSnmCkT1fZXDz8BkN5RRYe9Zrjy)
51. [calcalistech.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqL_LaJg2OqRbyX3TDLBsmKvmLnDojwSYT7D5i6UPsCB2hJ0N982yrwmF1ZyckiwO_kgfMaBSUwGu42_8BVeNpyTkCko-MleJ43Nro8DE9h8cJQ9zDBw7hb1DMk47gL7MSo0RO0FS79mgKbsjfVgap)
52. [nozominetworks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZsgLYq3YfQm1Y4tK40NDH4_Mqd3QAShKEt3bMdajVL_rjgh26yM5_KN8C8AcrEbAXR2j0bcpA_O6XbOt2DpxTbnqZBGuLhK31Dbm8Q7EeKVYdN2xbB-5b9Ejrq8ZnvbgV7YbcsjldDb-r0heK7xWhumoXtapf3xsy1gXksNDoTe47K6801GYAAha_hg==)
53. [nsa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7If3lx8XqICAeWAPKZH_W4OIT_t8k77Pkz7Z1UaOsh9FuTxkSU39ctrH935e4uGgz7YGbQg4MPogy_ru6KU1ZPEiBv0vY-0GwYDQ5OpZf6tMcunXFBJhLK6qrfKVd-D3nxz49hmvjRpqgVZ9iPlgZemz-2e4Q0rEYybHJTAJeAWTjNOxvpJm2vnSlkY-6Pxm3WeCh-3c3Gq4fYKo8ICYJ90KecunK9xssDgU3P4lADEkWkomISIQkJ2rI-emD6pAoXBtuUOiMNM_lFfjcohZach8dSDhL4dxz9BagY5GBHR7M9g==)
54. [zscaler.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn_rWrYt8TpdpCjVTKrsUVI4k1jhltFlgqkjHhCPUiAa2EJXkqgHyzcPh6TgQ1dLqgMo-sxi2_GMEDwH8-Gs3lFgdceCAD8NDES6GjVUMnerRCdKHGqz2kvaxqE0f4DJV7i8VEBE1iyQHKHou7McxTK0Qfm0O0b-N5EkLLVZU=)
55. [fortinet.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERAlTMfrxAMGRQTNTg9HNsmBS-RZKCR6XcyvtT16cb7vkd8G61VjXvMf4sY9VJ-baKf6zi5kOj0Q7_PxPiMagpov6EP5vwQbIQIae9BiS-l28GGG-yYTLYM0mguXCFFBtbwDeGLrHHjmeDbKdaeTVF7VAx4s2Q_ld2H9S_0zvIsh3IXMlbdXWkWyaSSY0tmZdyl6Zl0BF_pmcP1OH8XZuA43RV6EY6Mvt5ucnpoan_iLhwKO94XxhIortySA45hQo=)
