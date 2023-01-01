from django.db import models
from django.utils import timezone

# Create your models here.
class Coordinator(models.Model):#QuerySet
    STARS = (
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    )
    name = models.CharField('氏名', max_length=255)
    furigana = models.CharField('ふりがな', max_length=255)
    picture = models.CharField('写真', max_length=255)
    text = models.TextField('メッセージ')
    stars = models.IntegerField('星の数', choices=STARS)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    # 追加 管理画面の登録情報の表示名を変える
    def __str__(self):
        return '名前：{}'.format(self.name)

        

class Coordinator2(models.Model):#QuerySet
    STARS = (
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    )
    name = models.CharField('氏名', max_length=255)
    furigana = models.CharField('ふりがな', max_length=255)
    picture = models.CharField('写真', max_length=255)
    text = models.TextField('メッセージ')
    stars = models.IntegerField('星の数', choices=STARS)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    # 追加 管理画面の登録情報の表示名を変える
    def __str__(self):
        return '名前：{}'.format(self.name)