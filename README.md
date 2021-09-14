# helpdesk2opp

Links helpdesk.ticket to crm.lead module via many2one and one2many relation

Buttons added to helpdesk.ticket module:
- Create Opportunity; Adds a pop-up from which the user can create a CRM Opportunity and automatically links current ticket to created CRM Opp.
- Link Opportunity; Adds a pop-up from which the user can link the current ticket to already existing CRM Oppourtinities 
- View Opportunity; When clicked takes user to tree view of linked CRM Opp.

Buttons added to crm.lead module:
- Ticket(s) button from which the user can view current tickets that have been linked to the Opportunity