import re
from math import ceil


class ArticleReadTimeEngin:
    @staticmethod
    def word_count(text):
        words = re.findall(r"\w+", text)
        return len(words)

    @staticmethod
    def estimate_reading_time(
        article, word_per_minute=255, second_per_image=10, second_per_tag=2
    ):
        word_count_body = ArticleReadTimeEngin.word_count(article.body)
        word_count_title = ArticleReadTimeEngin.word_count(article.title)
        word_count_description = ArticleReadTimeEngin.word_count(article.description)
        total_word_count = word_count_body + word_count_title + word_count_description
        reading_time = total_word_count / word_per_minute
        if article.banner_image:
            reading_time += second_per_image / 60
        tag_count = article.tags.count()
        reading_time += (tag_count * second_per_tag) / 60
        reading_time = ceil(reading_time)
        return reading_time
