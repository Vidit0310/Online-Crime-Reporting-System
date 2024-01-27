
# Online Crime Reporting System Using Django
![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/home_page.png)

[OCRS](https://github.com/Prakash0405/OnlineCrimeReportingSystem)  Online Crime Reporting System, developed using Python Django, HTML, CSS, and JavaScript, aims to enhance crime reporting efficiency and communication between citizens and law enforcement agencies. The user interface enables citizens to securely register, manage profiles, and create detailed crime reports with specific categories and file uploads. Admins, through a centralized dashboard, oversee and verify complaints, assigning them to police stations. Police officers access secure login functionality, manage profiles, and update FIR and CSR statuses in real-time. The system, developed with Django Forms and Models, anticipates delivering a secure, user-friendly platform, contributing significantly to community safety.


## Features

### USER / CITIZEN
  
- Register
- Login
- Manage Profile
- Create complaint (select crime category and upload files.)
- View complaint status
- View FIR (with FIR No.)
- View CSR(with CSR No.)
     
 
 
### ADMIN / Headquarter

- Login
- Manage Profile
- Add Police Station (as per the cities)
- Create and manage crime category
- Create police user (as per the Police Station and their post)
- Manage police user (can also set their active/inactive and suspend status of police user of every station).
- Verify and Manage complaints (pass the complaint to the particular station incharge).
- View all reports ( CSR / FIR ) and complaints [Of all police stations]
- View Criminals Records and information (of all police stations)

- Create and Manage Announcements

    

    
### POLICE STATION INCHARGE

  
- Login
- Manage Profile

- View Complaint
- File FIR / CSR (as per the online complaint)
- Create FIR / CSR if complaint is done offline
- View all report ( CSR / FIR ) of station
- Manage police user’s status (can set their active/inactive and   suspend status)
- Assign the case to the police users or the group of police users
- View Announcements

### POLICE OFFICER


- Login
- Manage Profile
- View FIR
- View CSR
- Manage and Update status of FIR /CSR
- View all report ( CSR / FIR ) of station
- View and Manage Criminal Records of Station
- View Announcements


    
| Admin Dashboard | Police Incharge Dashboard | Police Officer Dashboard | User Dashboard |
| -------| -------| -------| -------|
| Email: `admin@admin.com` | Email: `thaltejpi@gov.in` |   Email: `thaltejpolice@gov.in` |   Email: `user@gamil.com` |
| Password: `123` |  Password: `123` |  Password: `123` |  Password: `123` |
| ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/admin_Dashboard.png)| ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/pi_Dashboard.png) |    ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/PO_Dashboard.png)  |    ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/user_Dashboard.png)  |

 
  
-----------------------------------------------


# GET STARTED

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Prakash0405/OnlineCrimeReportingSystem.git

$ cd Online_Crime_Reporting_System
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd Online_Crime_Reporting_System
(env)$ python manage.py runserver
```
For admin login: `http://127.0.0.1:8000/admin`

## Screenshots

|  ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/home_page.png)| ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/Log_in.png)| ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/register.png)| ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/user_Dashboard.png)|
|--------------| --------------|   --------------|  --------------|    
|  ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/admin_Dashboard.png)| ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/admin_login.png)| ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/manage_profile.png)| ![](https://github.com/Prakash0405/OnlineCrimeReportingSystem/blob/main/Screenshots/view_status.png)|

# The Project was developed using the following:

Python Version: 	`3.11.4`

Django Version: 	`4.1`





