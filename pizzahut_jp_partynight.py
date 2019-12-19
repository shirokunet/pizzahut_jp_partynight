#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--lang=ja')

driver = webdriver.Chrome(chrome_options=options)

# rendering waiting time
wait=WebDriverWait(driver,1)
driver.implicitly_wait(1)

# access to pizzahat
url = "https://pizzahut.jp/"
driver.get(url)
# driver.save_screenshot("top.png")


def click_xpath(webElement, loop=True):
    try:
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, webElement)))
        driver.find_element_by_xpath(webElement).click()
    except Exception as e:
        if loop:
            print("Could not find: ", webElement)
            print("Try again...")
            time.sleep(1)
            click_xpath(webElement)


if __name__ == '__main__':
    try:
        click_xpath("//*[text()='住所で検索']", loop=False)
    except Exception as e:
        print(e)

    time.sleep(1)
    e = driver.find_element_by_xpath("//*[@placeholder='住所']")
    e.send_keys("東京都千代田区外神田6丁目")
    e.send_keys(Keys.ENTER)

    time.sleep(1)
    click_xpath("//*[text()=' 東京都 千代田区 外神田 ６丁目 ']")

    pizza_list = ['(ツナマヨ／ベーコン／オニオン／コーン／トマトソース)'
       ,'(ペパロニサラミ／ベーコン／ピーマン／オニオン／トマトソース)'
       ,'(パイナップル／ベーコン／コーン／オニオン／トマトソース)'
       ,'(イタリアントマト／バジルソース／トマトソース)'
       ,'(ペパロニサラミ／トマトソース)'
       ,'(ゴーダチーズ／イタリアントマト／オニオン／パセリ／トマトソース)'
       ,'(組合せ) 「直火焼テリマヨチキン」「アイダホ風ほっくりポテマヨ」「ピザハットミックス」「グリル野菜ミックス」'
       ,'(組合せ) 「デラックス」「ハワイアン」「シーフードミックス」「ピザハット・マルゲリータ」'
       ,'(あらびきスライスソーセージ／ポテト／コーン／ブラックペッパー／パセリ／トマトソース／特製マヨソース)'
       ,'(ガーリック／ペパロニサラミ／イタリアンソーセージ／あらびきスライスソーセージ／ブラックペッパー／トマトソース)'
       ,'(グリル野菜ミックス<ズッキーニ・赤ピーマン・黄ピーマン・ナス>／セミドライチェリートマト／アスパラ／ガーリック／パルメザンチーズ／トマトソース)'
       ,'(ペパロニサラミ／イタリアンソーセージ／あらびきスライスソーセージ／ピーマン／オニオン／マッシュルーム／トマトソース)'
       ,'(テリヤキチキン／コーン／特製マヨソース／きざみ海苔<別添>)'

       # Here is special pizza.
       # ,'(組合せ) 「ガーリックミートグルメ」「海老マヨ明太シーフード」「シシリア風ミートソース」「Wベーコンのジェノベーゼ」'
       # ,'(組合せ) 「チーズミート」「モッツァレラ・デラックス」「テリヤキクリームチーズ」「カマンベール・シュリンプ」'
       # ,'(組合せ) 「特うまプルコギ」「デラックス」「ツナマイルド」「完熟トマトのチーズ＆チーズ」'
       # ,'(熟成ベーコン／ベーコン／イタリアントマト／ガーリック／パルメザンチーズ／バジルソース／ホワイトソース)'
       # ,'(エビ／イカ／ツナマヨ／ブロッコリー／オニオン／トマトソース)'
       # ,'(ガーリック／熟成ベーコン／イタリア産グリル野菜<ズッキーニ・赤ピーマン・黄ピーマン・ナス>／パルメザンチーズ／特製ミートソース)'
       # ,'(セミドライチェリートマト／バジルソース／フレッシュモッツァレラチーズ／トマトソース)'
       # ,'(ハラペーニョ／グリーンチリソース／あらびきスライスソーセージ／イタリアントマト／グリル野菜ミックス<ズッキーニ・赤ピーマン・黄ピーマン・ナス>／パルメザンチーズ／特製ミートソース)'
       # ,'(ベーコン／エビ／ポテト／オニオン／コーン／パセリ／特製マヨソース／オーロラソース)'
       # ,'(エビ／イカ／コーン／パセリ／明太クリームソース／特製マヨソース)'
       # ,'(プルコギ／ニラ／オニオン／辛口糸唐辛子／特製マヨソース)'
       # ,'(組合せ) 「特製ローストビーフ」「オマールシーフード」「プレミアム・マルゲリータ」「贅沢イベリコポテト」'
       # ,'(組合せ) 「海老マヨベーコン」「炭火焼ビーフカルビ」「とろける4種チーズのフォルマッジ」「プレミアム・マルゲリータ」※ハニーメイプル付'
       # ,'(ベーコン／ペパロニサラミ／イタリアンソーセージ／あらびきスライスソーセージ／マッシュルーム／ピーマン／オニオン／ブラックオリーブ／トマトソース)'
       # ,'(クリームチーズ／カマンベールチーズ／フレッシュモッツァレラチーズ／パルメザンチーズ／ブラックペッパー／チーズソース) ※ハニーメイプル付'
       # ,'(イベリコ豚の厚切ベーコン／熟成ベーコン／ペパロニサラミ／オニオン／ブラックペッパー／トマトソース)'
       # ,'(炭火焼牛カルビ／ピーマン／オニオン／ガーリック／辛口糸唐辛子)'
       ]

    for pizza in pizza_list:
        time.sleep(1)
        print("Let's order: ", pizza)
        click_xpath("//*[text()='ピザ全品 デリバリーで30%off']")
        click_xpath("//*[text()='ピザをお選びください（画像クリックで選択できます）']")
        click_xpath("//*[@title='" + pizza + "']")
        click_xpath("//*[text()='ふっくらパンピザ']")
        click_xpath("//*[text()='カートに入れる']")
        click_xpath("//*[text()='カートに商品を追加']")
        print("Done.")

    print("Finish!")
