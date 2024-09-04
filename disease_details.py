def get_disease_details(disease_name):
    disease_details = {
         'Apple Apple Scab': """
        **Apple Scab: Causes, Symptoms, and Management**

        **Introduction**
        Apple scab is a common fungal disease affecting apple trees, caused by the fungus *Venturia inaequalis*. 
        It is a significant concern for apple growers as it can lead to severe fruit blemishing and yield loss.

        **Symptoms:** Olive-green to black velvety spots appear on the leaves, leading to yellowing and premature leaf drop. 
        Dark, scabby lesions form on the fruit, making it unmarketable.

        **Fertilizer Recommendation**
        - Use a balanced fertilizer such as 10-10-10 or 12-12-12 to maintain healthy growth.

        **Pesticide Recommendation**
        - Apply fungicides like Captan or Mancozeb during the growing season.
        """,
        'Apple Black Rot': """
        **Black Rot on Apple: Causes, Symptoms, and Management**

        **Introduction**
        Black rot is a significant fungal disease affecting apple trees, caused by the fungus *Botryosphaeria obtusa*. 

        **Symptoms:** Dark, circular lesions on apples, which gradually enlarge, turning black and often forming concentric rings. 
        Infected fruit may shrivel and become mummified.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer such as 10-10-10, focusing on improving soil health.

        **Pesticide Recommendation**
        - Use fungicides such as Captan or Myclobutanil, especially during wet weather.
        """,
        'Apple Cedar Apple Rust': """
        **Cedar Apple Rust: Causes, Symptoms, and Management**

        **Introduction**
        Cedar apple rust is a fungal disease that affects apple trees and junipers, caused by *Gymnosporangium juniperi-virginianae*.

        **Symptoms:** Yellow-orange spots on apple leaves that eventually develop tube-like structures on the underside. 
        Fruit may develop similar lesions.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer such as 10-10-10.

        **Pesticide Recommendation**
        - Apply fungicides such as Myclobutanil and avoid planting near cedar trees.
        """,
        'Apple Healthy': """
        **Apple Tree Health Status:**

        **Condition:** Healthy

        **Notes:** Your apple tree is in good condition. Continue with the following care to maintain its health:

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with a ratio like 10-10-10 or 12-12-12 once per year in early spring.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Blueberry Healthy': """
        **Blueberry Plant Health Status:**

        **Condition:** Healthy

        **Notes:** Your blueberry plant is in good condition. Continue with the following care to maintain its health:

        **Fertilizer Recommendation**
        - Use an acid-forming fertilizer, such as ammonium sulfate, in spring.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Cherry (Including Sour) Healthy': """
        **Cherry Tree Health Status:**

        **Condition:** Healthy

        **Notes:** Your cherry tree is in good condition. Continue with the following care to maintain its health:

        **Fertilizer Recommendation**
        - Use a balanced fertilizer, like 10-10-10, in early spring.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Cherry (Including Sour) Powdery Mildew': """
        **Powdery Mildew on Cherry: Causes, Symptoms, and Management**

        **Introduction**
        Powdery mildew is a common fungal disease that affects cherry trees, caused by *Podosphaera clandestina*.

        **Symptoms:** White, powdery spots on leaves, which may curl and distort as the disease progresses.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer such as 10-10-10.

        **Pesticide Recommendation**
        - Use sulfur-based fungicides or potassium bicarbonate.
        """,
        'Corn (Maize) Cercospora Leaf Spot Gray Leaf Spot': """
        **Cercospora Leaf Spot on Corn: Causes, Symptoms, and Management**

        **Introduction**
        Cercospora leaf spot, also known as gray leaf spot, is a fungal disease caused by *Cercospora zeae-maydis*.

        **Symptoms:** Grayish or tan lesions on the lower leaves. Lesions may coalesce, leading to large, dead areas on the leaves.

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with adequate potassium to strengthen the plant against disease.

        **Pesticide Recommendation**
        - Apply fungicides such as strobilurins during early stages of infection.
        """,
        'Corn (Maize) Common Rust': """
        **Common Rust on Corn: Causes, Symptoms, and Management**

        **Introduction**
        Common rust is a fungal disease of corn, caused by *Puccinia sorghi*.

        **Symptoms:** Reddish-brown pustules appear on both sides of the leaves, which may coalesce and cause large areas of leaf tissue to die.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with sufficient nitrogen to promote healthy growth.

        **Pesticide Recommendation**
        - Use fungicides like Mancozeb or Propiconazole and rotate crops.
        """,
        'Corn (Maize) Healthy': """
        **Corn Plant Health Status:**

        **Condition:** Healthy

        **Notes:** Your corn plants are in good condition. Continue with the following care to maintain their health:

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with a higher nitrogen content, such as 20-10-10, during the growing season.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Corn (Maize) Northern Leaf Blight': """
        **Northern Leaf Blight on Corn: Causes, Symptoms, and Management**

        **Introduction**
        Northern leaf blight is a fungal disease affecting corn, caused by *Setosphaeria turcica*.

        **Symptoms:** Gray-green, elliptical lesions on the leaves that may become necrotic and lead to significant yield loss.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with adequate nitrogen to support the plant's defense mechanisms.

        **Pesticide Recommendation**
        - Use fungicides like Triazoles during early stages of infection.
        """,
        'Grape Healthy': """
        **Grapevine Health Status:**

        **Condition:** Healthy

        **Notes:** Your grapevines are in good condition. Continue with the following care to maintain their health:

        **Fertilizer Recommendation**
        - Use a balanced fertilizer, such as 10-10-10, in early spring.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Grape Black Rot': """
        **Black Rot on Grape: Causes, Symptoms, and Management**

        **Introduction**
        Black rot is a destructive fungal disease of grapevines, caused by *Guignardia bidwellii*.

        **Symptoms:** Small, circular, reddish-brown spots on leaves that develop black centers. Infected berries turn black and mummify.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with moderate nitrogen content.

        **Pesticide Recommendation**
        - Use fungicides like Mancozeb, particularly during wet weather.
        """,
        'Grape Esca (Black Measles)': """
        **Esca on Grape: Causes, Symptoms, and Management**

        **Introduction**
        Esca, also known as black measles, is a complex fungal disease affecting grapevines.

        **Symptoms:** Leaves may show interveinal chlorosis and necrosis, leading to a tiger-stripe pattern. Berries may develop dark streaks or spots.

        **Fertilizer Recommendation**
        - Use a balanced fertilizer to support overall vine health.

        **Pesticide Recommendation**
        - No specific fungicides are effective against Esca; focus on maintaining vine health through good cultural practices.
        """,
        'Grape Leaf Blight (Isariopsis Leaf Spot)': """
        **Leaf Blight on Grape: Causes, Symptoms, and Management**

        **Introduction**
        Leaf blight, caused by *Isariopsis clavispora*, primarily affects grape leaves.

        **Symptoms:** Brownish spots on leaves that expand and may cause the leaf to curl and drop prematurely.

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with adequate potassium.

        **Pesticide Recommendation**
        - Apply fungicides such as Captan during the growing season.
        """,
        'Orange Haunglongbing (Citrus Greening)': """
        **Citrus Greening on Orange: Causes, Symptoms, and Management**

        **Introduction**
        Citrus greening, also known as Huanglongbing (HLB), is a devastating bacterial disease affecting citrus trees.

        **Symptoms:** Yellowing of leaves in a blotchy, asymmetric pattern. Fruit may be small, misshapen, and bitter.

        **Fertilizer Recommendation**
        - Use a citrus-specific fertilizer with micronutrients to support the tree's health.

        **Pesticide Recommendation**
        - Focus on controlling the Asian citrus psyllid using insecticides; no cure exists for HLB.
        """,
        'Peach Bacterial Spot': """
        **Bacterial Spot on Peach: Causes, Symptoms, and Management**

        **Introduction**
        Bacterial spot is a destructive disease of peach trees, caused by *Xanthomonas campestris pv. pruni*.

        **Symptoms:** Water-soaked spots on leaves that turn brown and may lead to leaf drop. Fruit may develop scabby lesions.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer in early spring.

        **Pesticide Recommendation**
        - Use copper-based bactericides during wet weather.
        """,
        'Pepper, Bell Bacterial': """
        **Bacterial Spot on Bell Pepper: Causes, Symptoms, and Management**

        **Introduction**
        Bacterial spot is a common disease affecting bell peppers, caused by several species of *Xanthomonas*.

        **Symptoms:** Water-soaked spots on leaves that turn brown and become necrotic. Fruit develops raised, scabby lesions.

        **Fertilizer Recommendation**
        - Use a balanced fertilizer, such as 10-10-10, to support healthy growth.

        **Pesticide Recommendation**
        - Apply copper-based bactericides during periods of wet weather.
        """,
        'Pepper, Bell Healthy': """
        **Bell Pepper Plant Health Status:**

        **Condition:** Healthy

        **Notes:** Your bell pepper plants are in good condition. Continue with the following care to maintain their health:

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer, such as 10-10-10, during the growing season.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Potato Early Blight': """
        **Early Blight on Potato: Causes, Symptoms, and Management**

        **Introduction**
        Early blight is a common fungal disease of potatoes, caused by *Alternaria solani*.

        **Symptoms:** Dark, concentric rings on lower leaves forming a target-like pattern. Leaves may yellow and drop prematurely.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with moderate nitrogen content, such as 10-10-10.

        **Pesticide Recommendation**
        - Use fungicides like Chlorothalonil during periods of wet weather.
        """,
        'Potato Healthy': """
        **Potato Plant Health Status:**

        **Condition:** Healthy

        **Notes:** Your potato plants are in good condition. Continue with the following care to maintain their health:

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with higher potassium content, such as 5-10-10, during tuber development.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Potato Late Blight': """
        **Late Blight on Potato: Causes, Symptoms, and Management**

        **Introduction**
        Late blight is a devastating fungal disease of potatoes, caused by *Phytophthora infestans*.

        **Symptoms:** Dark, water-soaked lesions on leaves and stems, which quickly expand and turn black. Infected tubers develop firm, brown lesions that may rot.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with moderate nitrogen and high potassium content, such as 5-10-10.

        **Pesticide Recommendation**
        - Use fungicides such as Mancozeb or Metalaxyl during wet weather.
        """,
        'Raspberry Healthy': """
        **Raspberry Plant Health Status:**

        **Condition:** Healthy

        **Notes:** Your raspberry plants are in good condition. Continue with the following care to maintain their health:

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer, such as 10-10-10, in early spring.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Soybean Healthy': """
        **Soybean Plant Health Status:**

        **Condition:** Healthy

        **Notes:** Your soybean plants are in good condition. Continue with the following care to maintain their health:

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with sufficient nitrogen, phosphorus, and potassium.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Strawberry Healthy': """
        **Strawberry Plant Health Status:**

        **Condition:** Healthy

        **Notes:** Your strawberry plants are in good condition. Continue with the following care to maintain their health:

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with higher phosphorus content, such as 5-10-10, to promote flowering and fruiting.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Strawberry Leaf Scorch': """
        **Leaf Scorch on Strawberry: Causes, Symptoms, and Management**

        **Introduction**
        Leaf scorch is a fungal disease affecting strawberries, caused by *Diplocarpon earlianum*.

        **Symptoms:** Small, reddish-purple spots on leaves that enlarge and coalesce, leading to large, dead areas. In severe cases, leaves may die back completely.

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with moderate nitrogen content, such as 10-10-10.

        **Pesticide Recommendation**
        - Apply fungicides like Captan during wet weather.
        """,
        'Tomato Spider Mites Two-Spotted Spider Mite': """
        **Spider Mites on Tomato: Causes, Symptoms, and Management**

        **Introduction**
        Spider mites are tiny arachnids that can cause significant damage to tomato plants, particularly during hot, dry weather.

        **Symptoms:** Leaves may develop a stippled, yellowed appearance, with fine webbing often visible on the undersides.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with sufficient potassium to strengthen plant resistance.

        **Pesticide Recommendation**
        - Use insecticidal soap or neem oil to control mite populations.
        """,
        'Tomato Early Blight': """
        **Early Blight on Tomato: Causes, Symptoms, and Management**

        **Introduction**
        Early blight is a common fungal disease affecting tomatoes, caused by *Alternaria solani*.

        **Symptoms:** Dark, concentric rings appear on the lower leaves, forming a target-like pattern. The leaves may yellow and drop prematurely.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with moderate nitrogen content, such as 10-10-10.

        **Pesticide Recommendation**
        - Use fungicides like Mancozeb or Chlorothalonil during periods of wet weather.
        """,
        'Tomato Healthy': """
        **Tomato Plant Health Status:**

        **Condition:** Healthy

        **Notes:** Your tomato plants are in good condition. Continue with the following care to maintain their health:

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with slightly higher phosphorus content, such as 5-10-10, to promote fruiting.

        **Pesticide Recommendation**
        - No pesticides needed, but regular monitoring for any signs of pests or diseases is advised.
        """,
        'Tomato Leaf Mold': """
        **Leaf Mold on Tomato: Causes, Symptoms, and Management**

        **Introduction**
        Leaf mold is a fungal disease affecting tomatoes, caused by *Passalora fulva*.

        **Symptoms:** Yellow spots on the upper leaf surface that develop into grayish-brown mold on the underside of the leaves.

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with moderate nitrogen content.

        **Pesticide Recommendation**
        - Apply fungicides like Chlorothalonil during wet weather.
        """,
        'Tomato Tomato Mosaic Virus': """
        **Tomato Mosaic Virus: Causes, Symptoms, and Management**

        **Introduction**
        Tomato mosaic virus (ToMV) is a highly contagious viral disease affecting tomatoes, caused by a strain of the tobacco mosaic virus.

        **Symptoms:** Mottling, yellowing, and curling of the leaves, often leading to a "fern-like" appearance. Infected plants may be stunted and less vigorous.

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with sufficient nitrogen and potassium.

        **Pesticide Recommendation**
        - No chemical treatment available. Focus on strict sanitation practices to prevent the spread.
        """,
        'Tomato Target Spot': """
        **Target Spot on Tomato: Causes, Symptoms, and Management**

        **Introduction**
        Target spot is a fungal disease affecting tomatoes, caused by *Corynespora cassiicola*.

        **Symptoms:** Dark spots with concentric rings appear on the leaves, which may coalesce and cause large areas of leaf tissue to die.

        **Fertilizer Recommendation**
        - Apply a balanced fertilizer with moderate nitrogen content.

        **Pesticide Recommendation**
        - Use fungicides like Difenoconazole during periods of wet weather.
        """,
        'Tomato Tomato Yellow Leaf Curl Virus': """
        **Tomato Yellow Leaf Curl Virus: Causes, Symptoms, and Management**

        **Introduction**
        Tomato yellow leaf curl virus (TYLCV) is a viral disease affecting tomatoes, transmitted by the whitefly *Bemisia tabaci*.

        **Symptoms:** Yellowing and curling of the leaves, particularly in the upper canopy. Infected plants may become stunted and fail to produce fruit.

        **Fertilizer Recommendation**
        - Use a balanced fertilizer with sufficient nitrogen and potassium.

        **Pesticide Recommendation**
        - Focus on controlling whiteflies using insecticides and yellow sticky traps. No cure exists for TYLCV.
        """
    }
    
    return disease_details.get(disease_name, "Detailed information not available for this disease.")
