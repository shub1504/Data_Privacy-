# Practical 1: Data Privacy Audit of GeeksforGeeks

## Aim - To conduct a data privacy audit of the GeeksforGeeks website and identify how user data is collected, used, stored, and protected.

### Website Selected

#### Organization: L'Oreal
#### Website: https://brandstorm.loreal.com/en/challenges/india/community#
#### Privacy Policy: GFG Privacy Policy⁠

### Requirements
download the source code from this file 
install BeautifulSoup using the following command 

             pip install beautifulsoup4 requests


###Source code 

https://github.com/shub1504/Data_Privacy-/blob/main/privacy_audit.md/privacy_audit.py

###Conclusion 

A passive privacy and security audit of the L'Oréal Brandstorm India community page (https://brandstorm.loreal.com/en/challenges/india/community) was performed using a custom Python script, supported by a manual review of the site's privacy policy (https://brandstorm.loreal.com/en/privacy).

Strengths observed:

The site is served over HTTPS, so data in transit is encrypted.
Content-Security-Policy, X-Frame-Options, X-Content-Type-Options and Referrer-Policy headers are present, reducing the risk of XSS, clickjacking, MIME sniffing and referrer leakage.
The only cookie observed (__cf_bm, set by Cloudflare for bot management) has both the Secure and HttpOnly flags enabled.
No third-party scripts or known trackers were detected in the page source.
A privacy policy is available and is clear and transparent. It lists the data collected, purposes, legal basis for each purpose, retention period (maximum 2 years for account data), third-party sharing, hosting location (Europe) and a full set of user rights (access, rectification, erasure, objection, portability, restriction, consent withdrawal and complaint). It also states that personal data is not sold.

Gaps observed:

The Strict-Transport-Security (HSTS) header was not found in the response, which may expose users to protocol downgrade attacks. Recommendation: enable HSTS with an appropriate max-age.
The policy is based on GDPR and does not mention India's Digital Personal Data Protection (DPDP) Act, 2023, even though the page targets Indian users. Cross-border transfer of Indian users' data to Europe is also not addressed. Recommendation: add DPDP-compliant notice and consent language.
Retention periods are clearly stated only for account data and are vague for other categories.
Security measures are described in generic terms ("reasonable precautions") without specifics.
No named Data Protection Officer or grievance officer was found, only a general contact email.
Access requests may take up to three months and may attract a fee.

Limitations:
The script reads only static HTML. Because the page is rendered with JavaScript, it reported privacy_policy_link: false even though a privacy policy exists. This shows that automated results for forms, consent banners and footer links are inconclusive and need manual verification. The cookie consent banner and third-party network requests were not verified in this audit, and backend data storage, retention and access controls cannot be assessed through a passive scan.

Overall: The site follows good baseline security and transparency practices, with HSTS and DPDP Act alignment as the main areas for improvement. The audit also shows that automated scanning works best when combined with manual review.
