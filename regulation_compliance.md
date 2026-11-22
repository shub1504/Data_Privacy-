# Practical 3: Regulation Compliance (DPDP Act, 2023)
 
## Aim
To explore the requirements of data protection regulations (India's Digital Personal Data Protection Act, 2023, with the EU's GDPR for comparison) and to develop a compliance plan for an organisation.
 
> **Note:** The organisation assessed here is a *typical ride-hailing platform* (continuing from Practical 2). The gap analysis is illustrative and based on general industry practice. It makes no claim about any real company's internal practices. The Rules under the DPDP Act are being brought into force in phases, so exact deadlines should be confirmed from the official source (MeitY) before relying on them.
 
---
 
## Step 1: Regulation Overview
 
| Item | Details |
|---|---|
| Primary regulation | Digital Personal Data Protection (DPDP) Act, 2023 (India) |
| Scope | Processing of digital personal data within India, and processing outside India if it relates to offering goods or services to people in India |
| Comparison regulation | General Data Protection Regulation (GDPR), European Union |
| Regulator (India) | Data Protection Board of India |
 
### Key terms
| Term | Meaning |
|---|---|
| Data Principal | The individual to whom the personal data relates (rider, driver) |
| Data Fiduciary | The organisation that decides the purpose and means of processing (the platform) |
| Data Processor | An entity that processes data on behalf of a Data Fiduciary (cloud host, payment gateway) |
| Significant Data Fiduciary (SDF) | A Data Fiduciary notified by the government based on volume and sensitivity of data, risk to individuals and other factors. It has additional duties |
 
---
 
## Step 2: Key Requirements
 
| Area | DPDP Act, 2023 | GDPR (for comparison) |
|---|---|---|
| Consent | Free, specific, informed, unconditional and unambiguous; notice must be given before consent; consent can be withdrawn | Similar, but consent is only one of six legal bases (contract, legal obligation, legitimate interest, etc.) |
| Purpose limitation | Data used only for the purpose for which consent was given (or for specified "legitimate uses") | Same principle |
| Data minimisation | Collect only what is necessary for the stated purpose | Same principle |
| Storage limitation | Erase data when the purpose is served or consent is withdrawn, unless law requires retention | Same principle |
| Data Principal rights | Access to information, correction and erasure, grievance redressal, right to nominate another person | Wider set: access, rectification, erasure, restriction, portability, objection, automated decision-making |
| Security safeguards | Reasonable security safeguards to prevent a personal data breach | Appropriate technical and organisational measures |
| Breach notification | Notify the Data Protection Board and each affected Data Principal | Notify the supervisory authority within 72 hours |
| Children's data | Verifiable parental consent for persons under 18; no tracking, behavioural monitoring or targeted advertising directed at children | Parental consent below a set age (16, which member states may lower to 13) |
| Significant Data Fiduciary | Appoint a Data Protection Officer based in India, appoint an independent data auditor, conduct periodic Data Protection Impact Assessments | DPO and DPIA required in specified cases |
| Cross-border transfer | Allowed, except to countries the government restricts | Requires a transfer mechanism (adequacy decision, standard contractual clauses, etc.) |
| Penalties | Up to INR 250 crore (for example, failure to maintain reasonable security safeguards) | Up to EUR 20 million or 4% of global annual turnover, whichever is higher |
 
---
 
## Step 3: Gap Analysis (Ride-Hailing Platform)
 
Status key: **Compliant** (typically in place), **Partial** (in place but incomplete), **Gap** (commonly missing or weak). Statuses are assumed for a typical platform and link to the risks in Practical 2.
 
| # | Requirement | Typical status | Observation |
|---|---|---|---|
| 1 | Clear notice before consent, in plain language (and available in regional languages) | Partial | Permission prompts exist, but purposes of location use are often not specific |
| 2 | Free, specific and withdrawable consent for location and marketing | Partial | Consent for marketing should be separate and optional |
| 3 | Purpose limitation (location not reused for ads or profiling without consent) | Gap | Risk of purpose creep (Practical 2, R3) |
| 4 | Data minimisation (no location collection outside active trips) | Gap | Background collection is a risk (R1) |
| 5 | Defined retention and erasure of trip and location data | Partial | Retention periods are often vague or long (R7) |
| 6 | Reasonable security safeguards (encryption, access control, monitoring) | Partial | Insider access and breach risks remain (R4) |
| 7 | Breach notification process (Board and affected users) | Gap | Needs a documented, rehearsed incident response plan |
| 8 | Data Principal rights: access, correction, erasure | Partial | In-app account deletion and data access must be easy to find |
| 9 | Grievance redressal officer with published contact details | Partial | Must be clearly published and respond within the prescribed time |
| 10 | Children's data (age verification, parental consent) | Gap | Age checks are often weak for riders |
| 11 | Data processing agreements with processors (cloud, payment, maps) | Partial | Contracts should bind processors to the same obligations |
| 12 | Cross-border transfer controls | Partial | Must check government restrictions on destination countries |
| 13 | SDF obligations (India-based DPO, independent audit, DPIA) if notified as an SDF | Partial | A large platform handling location data at scale is likely to be considered |
 
---
 
## Step 4: Compliance Plan
 
| Priority | Action | Addresses | Owner | Timeline |
|---|---|---|---|---|
| High | Rewrite privacy notice in plain language with a specific purpose for each data category; offer it in regional languages | #1 | Legal / Privacy team | 1 month |
| High | Restrict location collection to active trips and in-app use; remove background tracking | #4 | Engineering | 1-2 months |
| High | Separate, optional consent for marketing and analytics; enforce purpose tags in the data pipeline | #2, #3 | Product / Engineering | 2 months |
| High | Create and rehearse a breach response plan (detect, contain, assess, notify Board and users) | #7 | Security team | 2 months |
| High | Encrypt data in transit and at rest; role-based access control; log and review employee access to location data | #6 | Security team | 3 months |
| Medium | Publish retention schedule; auto-delete or anonymise expired data; coarser location generalisation (e.g. H3) for analytics | #5 | Data / Engineering | 3 months |
| Medium | Add in-app tools to view, correct, download and delete data; publish grievance officer details | #8, #9 | Product / Legal | 3 months |
| Medium | Age gating and verifiable parental consent flow; disable tracking and targeted ads for minors | #10 | Product / Legal | 3-4 months |
| Medium | Update contracts with processors; maintain a register of third parties and cross-border transfers | #11, #12 | Legal / Procurement | 3-4 months |
| Medium | Assess SDF status; appoint India-based DPO, independent auditor and schedule periodic DPIAs | #13 | Leadership / Legal | 6 months |
| Ongoing | Staff training, periodic internal audit and compliance review | All | Compliance team | Continuous |
 
---
 
## Step 5: Conclusion
 
The DPDP Act, 2023 places the responsibility for lawful, fair and transparent processing on the Data Fiduciary, with consent, purpose limitation, data minimisation, storage limitation, security safeguards, breach notification and Data Principal rights at its core. Compared with the GDPR, the DPDP Act relies mainly on consent (with limited legitimate uses), has fewer individual rights, but is explicit about children's data and the extra duties of Significant Data Fiduciaries.
 
The gap analysis of a typical ride-hailing platform shows that the largest gaps relate to location data: purpose creep, collection outside active trips, retention, breach response and age verification. The compliance plan prioritises these items, followed by data principal rights, processor contracts, cross-border controls and SDF obligations. Continuous training, audits and periodic review are needed because the Rules and guidance under the Act continue to develop. With these measures the platform can reduce its legal exposure and, more importantly, protect the privacy of riders and drivers.
 
