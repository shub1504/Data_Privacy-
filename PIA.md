# Practical 2: Privacy Impact Assessment (PIA) of a Ride-Hailing Platform
 
## Aim
To conduct a Privacy Impact Assessment of a typical ride-hailing platform (such as Uber) in order to identify privacy risks to individuals, particularly those arising from location data, and to propose measures to mitigate them.
 
> **Note:** This assessment is based on publicly available information and general industry practice (for example, Uber's open-source H3 hexagonal grid system). It does not claim knowledge of any company's internal systems.
 
## Tools / References
- Digital Personal Data Protection (DPDP) Act, 2023 (India)
- H3 hexagonal geospatial indexing system (open source, originally developed by Uber)
- Risk matrix (Likelihood x Impact)
---
 
## Step 1: System Description
A typical ride-hailing platform matches riders with nearby drivers in real time. The platform continuously collects location data from rider and driver devices, maps coordinates to a hexagonal grid index (e.g. H3) for efficient matching, and tracks trips from pickup to drop-off.
 
| Item | Details |
|---|---|
| Data subjects (Data Principals) | Riders and drivers |
| Data controller (Data Fiduciary) | Platform operator |
| Other parties | Payment gateways, mapping/cloud providers, communication (call/SMS) providers, regulators/law enforcement |
| Purpose | Match riders with nearby drivers, calculate routes and fares, ensure safety, prevent fraud |
 
## Step 2: Data Inventory
 
| Data category | Examples | Collected from |
|---|---|---|
| Identity | Name, phone, email, profile photo | Rider, Driver |
| Driver documents | Driving licence, vehicle registration | Driver |
| **Location data** | Live latitude/longitude pings, timestamp, pickup/drop-off addresses, trip route, H3 cell ID | Rider, Driver |
| Trip data | Trip history, duration, distance, ratings | Both |
| Payment | Card/UPI details, fare, transaction history | Rider |
| Device data | IP address, device ID, OS | Both |
| Communication | In-app chat/call logs | Both |
 
### How location data is represented
The app periodically sends a time-stamped record to the server:
 
```
(user_id, latitude, longitude, timestamp)
```
 
The server converts each coordinate into an **H3 cell ID** (a hexagon covering a small area). Matching looks for drivers in the rider's cell and its neighbouring cells, since every neighbour of a hexagon is equidistant from its centre.
 
## Step 3: Data Flow, Legal Basis and Necessity
 
### Data flow
1. User grants the location permission on the device (consent).
2. Device sends `(user_id, lat, lng, timestamp)` to the platform backend at regular intervals.
3. Backend converts coordinates to an H3 cell ID and passes it to the matching service.
4. Matching service finds nearby drivers in the rider's cell and neighbouring cells.
5. During the trip, route and location updates are stored in the trip database.
6. Data is shared with third parties (payment gateway, maps provider, cloud host, communication provider).
7. After the retention period, data should be deleted or anonymised.
```
Rider/Driver device --(location permission)--> Platform backend
   --> H3 indexing & matching service --> Trip database
   --> Third parties (payment, maps, cloud, communication)
   --> Retention / deletion or anonymisation
```
 
### Legal basis (DPDP Act, 2023)
The platform acts as a Data Fiduciary and riders/drivers are Data Principals. Location data is collected on the basis of consent given through the device's location permission prompt.
 
| Principle | Application to a ride-hailing platform |
|---|---|
| Notice and consent | Clear notice on what is collected and why; consent must be free, specific, informed and withdrawable |
| Purpose limitation | Location used only for matching, routing and safety; advertising or profiling needs separate consent |
| Data minimisation | Collect only what is necessary; no continuous tracking outside active trips |
| Storage limitation | Delete or anonymise data once the purpose ends (except legal retention) |
| Security safeguards | Encryption, access control, breach detection |
| Breach notification | Notify the Data Protection Board and affected users |
| Data Principal rights | Access, correction, erasure, grievance redressal |
| Children's data | Verifiable parental consent for under-18s; no tracking or behavioural monitoring of children |
 
### Necessity test
| Data / practice | Necessary? |
|---|---|
| Live location during an active trip | Yes (matching, navigation, safety) |
| Location when the app is not in use | No (excess collection) |
| Trip history for disputes/legal needs | Yes, for a limited period only |
| Access to the phone's contact list | No |
| Use of location history for ads/profiling | No (purpose creep) |
 
## Step 4: Risk Identification
 
Likelihood and impact are rated Low / Medium / High.
 
| ID | Risk | Likelihood | Impact | Rating |
|---|---|---|---|---|
| R1 | **Excessive collection:** background location collected when no trip is active | Medium | High | High |
| R2 | **Profiling from location history:** home, workplace, daily routine, and visits to sensitive places (hospitals, places of worship) can be inferred | High | High | High |
| R3 | **Purpose creep:** location data reused for advertising or analytics without separate consent | Medium | Medium | Medium |
| R4 | **Data breach or insider misuse:** unauthorised access to live and historical locations | Medium | High | High |
| R5 | **Re-identification:** even generalised H3 cell trails, linked with timestamps, can reveal a person's routine | Medium | High | High |
| R6 | **Third-party sharing / cross-border transfer** without clear disclosure | Medium | Medium | Medium |
| R7 | **Excessive retention** of trip and location data | Medium | Medium | Medium |
| R8 | **Stalking or safety risk:** a driver or rider retaining the other party's pickup/home address after the trip | Medium | High | High |
| R9 | **Weak notice and user control:** unclear consent, hard-to-find controls, no easy withdrawal or deletion | Medium | Medium | Medium |
 
### Risk matrix (Likelihood x Impact)
 
| | Low impact | Medium impact | High impact |
|---|---|---|---|
| **High likelihood** | | | R2 |
| **Medium likelihood** | | R3, R6, R7, R9 | R1, R4, R5, R8 |
| **Low likelihood** | | | |
 
## Step 5: Mitigation Measures
 
| Risk | Mitigation | Residual risk |
|---|---|---|
| R1 | Collect location only while the app is in use or during an active trip; no background tracking; request the minimum permission level | Low |
| R2 | Limit retention of precise location history; aggregate or generalise old data; give users a way to view and delete history | Medium |
| R3 | Strict purpose limitation; separate, optional consent for any marketing or analytics use; internal audit of data use | Low |
| R4 | Encryption in transit and at rest; role-based access control; logging and monitoring of employee access; breach response plan | Medium |
| R5 | Generalise location using H3 cells at a coarser resolution; avoid storing fine-grained timestamped trails longer than needed; add noise or aggregation before analytics | Medium |
| R6 | Disclose all categories of third parties; data processing agreements; document and assess cross-border transfers under the DPDP Act | Low |
| R7 | Define and publish retention periods; automatic deletion or anonymisation when the period ends | Low |
| R8 | Hide exact pickup/drop-off addresses from the other party after trip completion; mask phone numbers through proxy numbers; in-app safety reporting | Low |
| R9 | Clear, layered privacy notice; granular consent; easy withdrawal; accessible grievance officer | Low |
 
### Privacy-by-design demonstration: location generalisation with H3
Storing an H3 cell instead of the exact point reduces how precisely a person can be located.
 
```python
# pip install h3
import h3
 
lat, lng = 28.6139, 77.2090            # exact location (sensitive)
cell = h3.latlng_to_cell(lat, lng, 8)  # resolution 8 is roughly 0.7 sq km
print("Exact point :", lat, lng)
print("H3 cell ID  :", cell)
print("Cell centre :", h3.cell_to_latlng(cell))
```
 
The exact point is replaced by a hexagon cell, and the cell centre returned is slightly different from the original point. (In older versions of the `h3` library the function is named `geo_to_h3`.)
 
## Step 6: Conclusion and Residual Risk
 
The assessment of a typical ride-hailing platform shows that location data is the most privacy-sensitive element of the system. Although live location during an active trip is necessary for matching, navigation and safety, practices such as background collection, long retention of location history, reuse for advertising and weak notice create serious risks. Location trails, even when generalised into H3 hexagon cells, can reveal a person's home, workplace and routine, so generalisation reduces but does not remove the risk of re-identification.
 
The proposed measures (minimum necessary collection, purpose limitation, defined retention periods, strong access control and encryption, location generalisation, address and phone masking, and clear consent with user control) reduce most risks to Low or Medium. The remaining **medium residual risks** are profiling from location history (R2), insider or breach-related misuse (R4) and re-identification from cell trails (R5). These require continuous monitoring, periodic audits and compliance with the DPDP Act, 2023.
 
**Overall:** The system can be operated in a privacy-respecting way provided the mitigations are implemented and reviewed regularly.
 
