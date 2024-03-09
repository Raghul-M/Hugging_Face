from transformers import pipeline

summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

text = """

India, a land of vibrant diversity and rich heritage, captivates the soul with its kaleidoscope of cultures, traditions, and landscapes. Nestled in the heart of South Asia, this vast nation stretches from the towering peaks of the Himalayas in the north to the sun-kissed beaches of the Indian Ocean in the south. With a history steeped in antiquity, India's story unfolds like an epic saga, woven with tales of conquests, empires, and spiritual enlightenment.

At the core of Indian identity lies its cultural mosaic, where countless languages, religions, and customs coexist in harmony. From the majestic forts of Rajasthan to the tranquil backwaters of Kerala, each region paints a unique tableau, offering a glimpse into its own distinct heritage. The bustling streets of Delhi echo with the footsteps of emperors and sages, while the serene temples of Varanasi stand as timeless monuments to faith and devotion.

India's culinary landscape is equally diverse, a tantalizing fusion of flavors and aromas that reflects its rich history of trade and conquest. From the fiery curries of the south to the savory street food of Mumbai, every dish tells a story, inviting travelers on a gastronomic journey through time.

But perhaps India's greatest treasure lies in its people, whose warmth and hospitality welcome visitors with open arms. Whether celebrating Diwali with fireworks and sweets or sharing a cup of chai on a bustling street corner, the spirit of camaraderie and kinship is palpable, binding the nation together in a tapestry of unity and diversity.

Yet, amid the vibrant tapestry of India's cultural landscape, challenges abound. Poverty and inequality cast a shadow over the nation's progress, while environmental degradation threatens the natural beauty that has long inspired poets and dreamers. Yet, in the face of adversity, India remains resilient, drawing strength from its ancient wisdom and unwavering spirit.

As the world marches forward into the 21st century, India stands at a crossroads, poised to embrace the opportunities of a rapidly changing world while staying true to its timeless values and traditions. With its rich tapestry of cultures, its vibrant democracy, and its unwavering spirit of resilience, India continues to inspire and captivate the imagination of the world, reminding us all of the enduring power of the human spirit.





"""

summarized_text=summarizer(text, min_length = 5,max_length=140)[0]["summary_text"]

print(summarized_text)