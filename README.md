# Alexa Voice Bot
Provides safety measures for Patients based on Symptoms

Technologies used
- Amazon Development Portal (ADP)
- Python Programming (flask API)
- AWS Zappa (for deployment)

### *Approach I*:
AWS lambda function instead of Zappa, faced difficulty with flask_ask integration

### *Approach II*:
Executed code locally and used ngrok to get a https URL but connection was not stable

### **Approach III**:
- Created a virtual environment and installed all the required dependencies.
- Created Lambda function using flask api of python.
- Created IAM account in AWS and deployed code using Zappa user which provides a static URL.
- Subscribed free tier Amazon developer account and created an Alexa skill.
- Provided JSON intentSchema to the Skill and built it.
- Configured skill with lambda function using Zappa provided URL.

Skill is now ready to test using *echosim.io* virtually or using devices like *Echo*, *Echo dot* physically by signing in with same *amazon account credentials*.

### **Future Scope**:
- Self Learning - **scikit** library implementation.
- Integrate with **Google Maps API** to find nearest clinic.

## Branching
Latest emhancements will be updated to Master branch for release.
1. `master` branch
    > 1. merge needs `Pull Request` review/approval.
    > 1. Once reviewed and merged with `develop`, raise `Pull Request` for `master` for enhancement to be made.

1. `develop` branch
    > 1. Create Enhancement wise branches out of it.
    > 1. Work enhancements wise contribution.
    > 1. Push latest code with `Pull Requests` and get reviewed.
    > 1. merge needs `Pull Requests` review/approval.