**Issue Summary**

- **Duration of outage:** 2023-10-20 12:00 PM - 2023-10-20 14:00 PM (2 hours)
- **Impact:** The Nginx web server was unable to handle the amount of traffic, resulting in a high number of failed requests. All users were affected.
- **Root cause:** The default ULIMIT for the Nginx process was too low.

**Timeline**

- 12:00 PM - Monitoring alerts indicate a sharp increase in the number of failed requests for the Nginx web server.
- 12:15 PM - investigated the failed requests and determine that they are caused by the Nginx process reaching its ULIMIT.
- 12:30 PM - applied a Puppet script to increase the ULIMIT for the Nginx process.
- 13:00 PM - The number of failed requests begins to decrease.
- 13:30 PM - The number of failed requests has returned to normal levels.
- 14:00 PM - The outage is declared resolved.

**Misleading investigation/debugging paths**

- Initially, suspected that the failed requests were caused by a problem with the application code. However, further investigation revealed that the problem was with the Nginx web server.
- Also considered the possibility that the failed requests were caused by a surge in traffic. However, this was ruled out after examining the traffic logs.

**Which team/individuals was the incident escalated to?**

The incident was escalated to the on-call SRE team. The SRE team worked with the web development team to identify and resolve the issue.

**How the incident was resolved**

The incident was resolved by increasing the ULIMIT for the Nginx process. The ULIMIT is a system-imposed limit on the number of open files that a process can have. The default ULIMIT for the Nginx process was too low, which was causing the process to reach its limit and fail requests.

**Root cause and resolution**

The root cause of the outage was the default ULIMIT for the Nginx process being too low. The issue was resolved by increasing the ULIMIT for the Nginx process.

**Corrective and preventative measures**

- The default ULIMIT for the Nginx process will be increased.
- Monitoring will be added to alert on high ULIMIT usage.
- A process will be implemented for automatically increasing the ULIMIT if it is reached.