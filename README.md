# Alexa Voice Bot
Offering safety measures for patients based on symptoms.

Technologies used:
- Amazon Development Portal (ADP)
- Python Programming (flask API)
- AWS Zappa (for deployment)

### *First Approach*:
Tried AWS lambda function instead of Zappa, but ran into issues with flask_ask integration.

### *Second Approach*:
Ran the code locally and used ngrok to get a https URL, but the connection wasn't stable.

### **Final Approach**:
- Set up a virtual environment and installed all necessary dependencies.
- Created a Lambda function using Python's flask api.
- Set up an IAM account in AWS and deployed the code using a Zappa user which provides a static URL.
- Subscribed to Amazon developer account's free tier and created an Alexa skill.
- Provided JSON intentSchema to the Skill and built it.
- Connected the skill with the lambda function using the URL provided by Zappa.

The skill is now ready for testing either virtually via *echosim.io* or physically using devices like *Echo*, *Echo dot* by signing in with the same *Amazon account credentials*.

### **Future Possibilities**:
- Self Learning - Implementing the **scikit** library.
- Integrating with the **Google Maps API** to find the nearest clinic.

## Branching
The latest enhancements will be updated to the Master branch for release.
1. `master` branch
    > 1. Merging requires a `Pull Request` review/approval.
    > 1. Once reviewed and merged with `develop`, raise a `Pull Request` for `master` for the enhancement to be implemented.

1. `develop` branch
    > 1. Create branches for each enhancement from this branch.
    > 1. Work on enhancement-specific contributions.
    > 1. Push the latest code with `Pull Requests` and get it reviewed.
    > 1. Merging requires a `Pull Request` review/approval.
