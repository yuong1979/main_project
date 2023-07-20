from django.core.management.base import BaseCommand
from main.models import Tag
from main.models import Topic

class Command(BaseCommand):
    help = 'Inject data into the database'

    def handle(self, *args, **options):
        # Your logic here

        print ("This function facilitates the injection of data into the database but does not require code in it")

####################################################################################
#### run this with "python manage.py data_injection_script" ########################
####################################################################################

data_tags = [
    "True Crime", 
    "Business",
    "Comedy",
    "Personal Development",
    "Technology",
    "Health and Wellness",
    "Science",
    "History",
    "Sports",
    "Education",
    "Arts and Culture",
    "Music",
    "Film and TV",
    "Politics",
    "Parenting",
    "Books and Literature",
    "Travel",
    "Food and Cooking",
    "Pop Culture",
    "Interviews",
    "Storytelling",
    "Entrepreneurship",
    "Motivation",
    "Self-Help",
    "Fitness",
    "Mental Health",
    "Relationships",
    "Leadership",
    "Marketing",
    "Startups",
    "Finance",
    "Military and Defense",
    "Agriculture",
    "Engineering",
    "Aviation",
    "Self Defense and Martial Arts",
    "Cryptocurrency",
    "Psychology",
    "Productivity",
    "Social Media",
    "Sustainability",
    "Environmental Issues",
    "Inspiration",
    "Career Development",
    "Fashion and Style",
    "Design",
    "Technology Trends",
    "Gaming",
    "Philosophy",
    "Artificial Intelligence",
    "Diversity and Inclusion",
    "Meditation",
    "Creativity",
    "Mindfulness",
    "Spirituality",
    "Language Learning",
    "Motivational Stories",
    "Animal Welfare",
    "Photography",
    "World News",
    "Current Affairs",
    "Comedy Improv",
    "Cultural Diversity",
    "Art and History",
    "Personal Finance",
    "Social Issues",
    "Communication Skills",
    "Writing and Publishing",
    "Science Fiction",
    "Time Management",
    "Sustainability Practices",
    "Healthy Eating",
    "Environmental Conservation",
    "Personal Growth",
    "Relationship Advice",
    "Happiness and Well-being",
    "Investing",
    "Innovation",
    "Success Stories",
    "Public Speaking",
    "Product Reviews",
    "Sports Analysis",
    "Comedy Sketches",
    "Book Reviews",
    "Tech News and Updates",
    "DIY Projects",
    "Creative Writing",
    "Cultural Commentary",
    "Adventure Travel",
    "Inspirational Interviews",
    "Leadership Development",
    "Motivational Quotes",
    "Women Empowerment",
    "Goal Setting",
    "Money Management",
    "Social Entrepreneurship",
    "Futurism",
    "Alternative Health",
    "Biographies",
    "LGBTQ+ Issues",
    "Home Improvement",
    "Cryptocurrency Investing",
    "Education Reform",
    "Music Production",
    "Social Media Marketing",
    "Remote Work",
    "Mindset and Beliefs",
    "Adventure Sports",
    "Cultural Festivals",
    "Technology Reviews",
    "Motivational Speaking",
    "Sustainable Living Tips",
    "Organic Gardening",
    "Wildlife Conservation",
    "Self-Care Practices",
    "Stress Management",
    "Student Life",
    "Science Fiction Literature",
    "Time Travel",
    "Sustainable Fashion",
    "Vegan and Plant-Based Lifestyle",
    "Positive Psychology",
    "Freelancing and Gig Economy",
    "Science Discoveries",
    "Personal Branding",
    "Small Business Strategies",
    "Spirituality and Mindfulness",
    "Language Teaching Methods",
    "Inspirational Stories",
    "Eco-Tourism",
    "Political Commentary",
    "Improvisational Comedy Techniques",
    "Wilderness Survival Skills",
    "Historical Figures and Events",
    "Financial Independence",
    "Effective Communication in Relationships",
    "Cultural Heritage Preservation",
    "Cybersecurity",
    "Stand-up Comedy",
    "Eco-Friendly Living",
    "Astronomy and Space Exploration",
    "DIY Home Decor",
    "Digital Marketing",
    "Sustainable Energy Solutions",
    "Motivational Leadership",
    "Virtual Reality and Augmented Reality",
    "Self-Reflection and Growth",
    "Exploring Cultural Traditions",
    "Psychological Thrillers",
    "Futuristic Technologies",
    "Nature Conservation Projects",
    "Public Policy Debates",
    "Improving Public Speaking Skills",
    "Entrepreneurial Success Stories",
    "Sustainable Architecture and Design",
    "Interior Design Inspiration",
    "Climate Change Solutions"
]





topic_tags = [
    "True Crime",
    "News and Current Affairs",
    "Personal Development",
    "History",
    "Science and Technology",
    "Business and Entrepreneurship",
    "Comedy and Entertainment",
    "Health and Wellness",
    "Pop Culture and Media",
    "Interviews and Conversations",
    "Travel and Adventure",
    "Sports",
    "Education and Learning",
    "Parenting and Family",
    "Art and Creativity"
]


# ### inserting the data into the tag model
# insertdata = [Tag(name=item) for item in data_tags]
# Tag.objects.bulk_create(insertdata)


# ### inserting the data into the topic model
# insertdata = [Tag(name=item) for item in topic_tags]
# Topic.objects.bulk_create(insertdata)


# # # Delete all topic
# Topic.objects.all().delete()




# # # Delete all tags
# Tag.objects.all().delete()
