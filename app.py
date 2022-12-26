import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Danielle Syse"
PAGE_ICON = ":wave:"
NAME = "Danielle Syse"
DESCRIPTION = """
Data Analytics Program Manager II, PgM for Google Cloud Open Source software projects with a detailed history in marketing and advertising.

Ex-Amazonian.
"""
EMAIL = "daniellesyse@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/desyse",
    "GitHub": "https://github.com/sysede",
    "Twitter": "https://github.com/sysedanielle"
}

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    image = Image.open('profile-pic.png')
st.image(image, width=150)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        file_name="CV.pdf",
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 8 Years expereince strategizing and producing large-scale marketing campaigns and data-story telling
- ✔️ Strong hands on experience and knowledge in HTML, CSS+, MySQL and Excel
- ✔️ Leadership experience in open-source software communities, developing brand awareness intiatives and problem-solving
- ✔️ Project Managament Certificate from Northwestern University, PmP certified
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: HTML, CSS+, MySQL, R, Stata
- 📊 Visulization: Adobe Creative, MS Excel, Plotly
- 📚 Marketing & Advertising: SEM, SEO, Social, Programmatic, Sponsored Search
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Program Manager II - Google via Adecco**")
st.write("01/2021 - Present")
st.write(
    """
Program Manager for community growth and engagement for the Open Source projects associated with multiple products in Google Cloud’s Data Analytics portfolio, specifically  Apache Beam, Apache Airflow, Apache Spark, Dataflow, and CDAP collectively representing over $XXX million in business annually
- ► Plan and execute paid and organic video, image, and text creative across social platforms to promote OSS project events and socialize new features, leading to an 6% increase in Maven Central Java downloads and a 48x increase in Go package downloads for Apache Beam
- ► Lead organizer for Beam Summit hybrid event,  including  managing upkeep of priorities, attendee outreach, event logistics, vendor management,  and leading internal stakeholder meetings with Beam Summit planning committee and external vendor event management team
- ► Improve and develop Apache Beam business processes as the main POC for Beam Meetups, Beam College, website development, Github blog posts, email cadence, community outreach, etc.
- ► Increased annual Beam Summit registrations via product marketing management by 17.2x since 2019 and 62% since 2021
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Creative & Campaign Manager | Amazon**")
st.write("02/2021 - 01/2022")
st.write(
    """
Primary POC  and project manager working directly with advertisers, external stakeholders, and internal Amazon partners throughout complex campaign executions with over $1MM in media spend for PepsiCo 2021 fiscal year
- ► Consult and strategize with Pepsi executives on creative strategy leveraging historical advertiser and industry data to deliver high quality engagements
- ► Develop data impact and lead process/product improvement projects with internal and external stakeholders (i.e. working with product team to refine current tools and products) to improve cross-vertical/cross-locale efficienc
- ► Lead and advised internal team and clientele for Pepsi’s marketing campaign at all aspects including design, ad-ops, sales, quality assurance, finance, account management teams
- ► Mentored clients and peers on Amazon products (including but not limited to Alexa, Shopping Ads, Fire TV, etc) and policies as well as industry trends to help optimize KPIs
- ► Pitched and secured additional $300K in budget for experimental closed-beta Fire TV ads for Propel that lead to a 35% increase in purchase rate, a 14x increase in ROAS, and a 1.8x subscribe-and-save increase
- ► Developed Alexa Audio Voice Service advertising beta opportunities with Amazon product team as a Subject Matter Expert that led to the first sale of $500K in media Q4 revenue from PepsiCo
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Media Manager | Fusion92**")
st.write("01/2020 - 02/2021")
st.write(
    """
Led paid search, paid social and sponsored search teams across 6 cost per goal & e-commerce clients including but not limited to financial institutions, food and beverage, and entertainment industries: Chicago Board of Options Exchange, Old Wisconsin, Buddig, Rivers Casino, OANDA, ADMIS, True Value
- ► Increased annual gross media budget by $250k for SEM via various pitches and performance
- ► Reported media findings and strategy suggestions to clients on a recurring basis
- ► Managed daily optimization schedules and increase performance for all accounts for paid search on major search engines, paid social, and sponsored search for grocery delivery
- ► Led paid search team, new hires and interns with best practices and techniques for paid media
- ► Increased ROAS by 58% for Buddig Sponsored Search campaigns within a month
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Paid Search Manager | Good Apple**")
st.write("05/2018 - 01/2020")
st.write(
    """
Managed 13+ SEM accounts with a focus on keyword prioritization strategies across the pharmaceutical and E-Commerce industry with over $2MM in gross SEM media spend  Clients included: Takeda, Medline, Dollar General, Treasury Winery, Greenwich Biosciences, Pure Storage, etc.
- ► Secured a $300k increase in incremental budget to utilize on SEM campaigns while improving monthly lead generation by 30% through strategy and optimization
- ► Provided reporting on a monthly and quarterly basis to clients including but not limited to language insights, performance data, and yearly strategic objectives
- ► Managed day to day contact with clients, various support agencies, and legal teams Analyzed and translate quantitative/qualitative data from SearchAds 360, Google & Microsoft Ads, & Google Analytics into strategic recommendations
- ► Implemented PPC strategies including geo-targeting for NPI Targets & conferences Assist in training employees for Good Apple SEM capabilities and tactics
"""
)

# --- Education & Accomplishments ---
st.write('\n')
st.subheader("Education & Accomplishments")
st.write(
    """

Northwestern University, Kellogg School of Business - Certificate in Agile Project Management
- ► June 2022 - September 2022

University of Wisconsin - Madison - B.A. in Sociology with focus on Data Analysis")
- ► September 2014 - May 2018
University of Wisconsin - Madison - B.A. in Journalism with dual concentrations in Strategic Communications and Reporting
- ► September 2014 - May 2018
University of Wisconsin - Madison - minor in Digital Studies with focus on computer programming and data privacy
- ► September 2014 - May 2018
"""
)
