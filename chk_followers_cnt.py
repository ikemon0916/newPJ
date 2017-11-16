# TEST GITHUB

# from selenium import webdriver
# from selenium.webdriver.common.by import By
import traceback
# import time
# import sys
# import math

import MySQLdb
from datetime import datetime

# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# parent_username = "__non.stagram__"      #筆文字（完了) 57     id 28
# parent_username = "fuku.yukari"          #筆文字（完了) 201    id 29
# parent_username = "sho_risoya"           #筆文字（完了) 289    id 30


# 処理対象親ユーザー
# arr_parent_username = ["dyyyna"]
# arr_parent_username = ["odeyu86"]


# 2017.8.28 ->   2017.8.22の残ユーザー  #イラストレーター    ★残あり★ 1848 "tamuroayano"のみ
# arr_parent_username = ["tamuroayano"]

# 2017.8.28  #キッチンドランカー  #ビール人妻部
# arr_parent_username = ["yukao83l","tamtam913","piano_chan_ff","k.kakamio","w_k_ooe_eoo","mitsumachi","chichan.73","yooshino.579n","yuiaki0817"]

# 未登録のユーザーのみセレクト
# arr_parent_username = ["tamtam913","piano_chan_ff","k.kakamio","mitsumachi","chichan.73","yuiaki0817"]
# 追加  #キッチンドランカー  #家呑み
# arr_parent_username = ["jikoman_meshi","k.makken","tamahaha1215","riiko69bbb","aoaoaabo","laulea0112","c.t.makanani","yo.shi.j"]
# arr_parent_username = ["yuiaki0817","jikoman_meshi","k.makken","tamahaha1215","riiko69bbb","aoaoaabo","laulea0112","c.t.makanani","yo.shi.j"]

# イラストレーター  残なし
# arr_parent_username = ["takashi.kuno","akkobaum","peggy_my","tomokasarumaru","ayamiyuun","chotchan_oka","mayuu_com"]

# スクラップブッキング
# arr_parent_username = ["camellia2575","nozomiphoto","kukki03","yukiyocolorful"]
# クロップパーティー
# arr_parent_username = ["matsuurasaori"]      #取得済み
# arr_parent_username = ["hachikaho","eikohara","tomomiiono"]
# クロップパーティー + イラストレーター
# arr_parent_username = ["hachikaho","eikohara","ayamiyuun","chotchan_oka","mayuu_com","tomomiiono"]

# 2017.8.30  #整理収納　残なし
# arr_parent_username = ["yuka.home","ayumi._.201","spoonhomeblog"]

# 整理収納アドバイザー
# arr_parent_username = ["otake_yoko","mio_radiant"]

# ハンドメイド布小物 #カルトナージュ
# arr_parent_username = ["lapetite_2015","lovingsmile_papi","uchi_coco","polarbears0320","ecru_gris","ciel.cartonnage","moon_dolce","nanananere_handmade","katakuli_","handmade_ajour","yyy6069","u39handmade"]

# 整理収納アドバイザー
# arr_parent_username = ["wagamichilife","bloomyoursmile","ourhome305"]
# arr_parent_username = ["ourhome305"]

# イラストレーター
# arr_parent_username = ["tkrknm518","mitsui.michiko","esk.s"]
# arr_parent_username = ["mitsui.michiko"]

# 手帳
# arr_parent_username = ["kakohiyori","ma.mimume.mo","takechiyo987"]

# 日記
# arr_parent_username = ["pufu_pp","mt230sh","non_sugar1011"]
# ダイアリー
# arr_parent_username = ["saezuri0808","hitotoki_official"]

# 素敵便
# arr_parent_username = ["hana116hana","atelier_yoco","asakusa_24","__ttu_3"]

# スタンピンアップ
# arr_parent_username = ["harukapapercraft","emiko_t_cardmaking","stamper.etsu","stamper.etsu","shiho.framboise.lemonade"]

# 整理収納アドバイザー   2017.9.1の残  ★残あり　"ourhome305"　2920
# arr_parent_username = ["ourhome305"]

# 整理収納アドバイザー
# arr_parent_username = ["kazu.t.0901","makelife_plus","tonoel","ie_gocochi","miyo_344"]

# 整理収納アドバイザー 追加(2017.9.8 未取得)
# arr_parent_username = ["_cocoti_","lovelyzakka"]
# arr_parent_username = ["kazu.t.0901","makelife_plus","tonoel","ie_gocochi","miyo_344","_cocoti_","lovelyzakka"]

# 2017.9.11
# 紙もの、ペーパーフラワー
# arr_parent_username = ["_c_h_e_r_i_","shamokoyuyuu","moningumi","totecoco","arcotum","mihiromaru"]

# 2017.9.12
# フラワーアレンジメント  ★残あり　hanajikan_magazine　4,577
# arr_parent_username = ["mitsu.stagram","ajitosaba","la_lune__rio","lemonleaf.jp","flowerlumiere","hanajikan_magazine"]

# 2017.9.13
# ほぼ日手帳(hachinosuke8)、イラストレーター（hisa_nishiya）
# arr_parent_username = ["hachinosuke8","hisa_nishiya"]

# 2017.9.14
# 切り絵アート
# arr_parent_username = ["jun.cutout","aikautau","itohchi","pon9232","ayaminbaby","northtaka"]

# 2017.9.15
# 腸活、美腸
# arr_parent_username = ["miyonce_25","nna1ono","bichokyoukai","cafeliliana","asuka1010ny","heart1016a","ayako1003"]
# arr_parent_username = ["ayako1003","makiron__s2","mayu.bberrycafe","yuiyoga"]


# 2017.9.18
# ヘアアレンジ
# arr_parent_username = ["aina.kt"]
# arr_parent_username = ["kimu3u0717","m351053m","kino.ko_hair_make","aina.kt"]

# 2017.9.20
# ほぼ日手帳　　#イラスト
arr_parent_username = ["packn0411", "mitsui.michiko", "esk.s"]

# 2017.9.21
# 日本茶専門店　　#日本茶   #和食　　#和食器
# arr_parent_username = ["usagiya","towaen_yusui","avacha","hyomu0917","rinmama1224","kazumi.kinoshita"]

# 2017.9.22
# エステサロン　#エステティシャン #ダイエット #産後ヨガ
# arr_parent_username = ["granverger","honaiwase","menard_love_h","lulur.ako2014","tsutsui.esthe","yaserepo","y1735k"]

# arr_parent_username = ["granverger","honaiwase","menard_love_h","lulur.ako2014","tsutsui.esthe","yaserepo","y1735k"]
# arr_parent_username = ["megumi_kanzaki","y1735k"]
# arr_parent_username = ["yaserepo","y1735k","megumi_kanzaki"]

# arr_parent_username = ["kimu3u0717","m351053m","kino.ko_hair_make","aina.kt"]
# arr_parent_username = ["aina.kt","hikaru027"]

# arr_parent_username = ["homei_nail"]

# 2017.9.27
# ほぼ日手帳　　#イラスト    ★残あり  5,037　　"mitsui.michiko","esk.s"]
# arr_parent_username = ["mitsui.michiko","packn0411","esk.s"]

# 和菓子　#日本の文化
# arr_parent_username = ["roccanao_ogawasadou","midori.muko","akihiro_nobuta","nagoya_kozakuraya"]


# 2017.9.28 #ママ美容師   #時短アレンジ #簡単アレンジ
# arr_parent_username = ["norikotouichi","a.y.a_21","yunagorigori","_mmm_aioi","403eri","michiko_k","sugenoaiko"]

# 2017.9.29 #整理収納アドバイザー　#整理整頓
# arr_parent_username = ["tomokokaneuchi","room.work","orie110","yurutanookataduke","uedmkk","aco.chaaaaan"]

# 2017.9.30 #整理整頓
# arr_parent_username = ["sumiko.home","yk.apari"]
# arr_parent_username = ["minmaro_0107","yk.apari"]
# arr_parent_username = ["yk.apari","minmaro_0107","sumiko.home"]
# arr_parent_username = ["tomokokaneuchi","room.work","orie110","yurutanookataduke","uedmkk","aco.chaaaaan","sumiko.home","yk.apari","minmaro_0107"]

# arr_parent_username = ["yk.apari", "minmaro_0107"]

# 整理収納アドバイザー　　2017.9.11 残あり　　"lovelyzakka"  6,061
# arr_parent_username = ["lovelyzakka"]

# megumi_kanzaki
# story_love40

# 2017.9.29 #整理収納アドバイザー　#整理整頓
# arr_parent_username = ["tomokokaneuchi","room.work","orie110","yurutanookataduke","uedmkk","aco.chaaaaan"]
# arr_parent_username = ["tomokokaneuchi","room.work","orie110","yurutanookataduke","uedmkk","aco.chaaaaan","sumiko.home","yk.apari","minmaro_0107"]
# arr_parent_username = ["yk.apari","minmaro_0107"]


# 2017.10.3
# 追加   #diy女子
# arr_parent_username = ["pandorahouse.wakayamamio","turners_milkpaint_official","____pir.y.o"]

# 2017.10.4
# イラストレーター
# arr_parent_username = ["esk.s", "illustrator_rikachan", "iwashikujira", "steven_spielhamburg"]

# arr_parent_username = ["esk.s"]

# 2017.10.5
# ミニチュア #ミニチュア雑貨
# arr_parent_username = ["orange_flower1210", "zakkabappy", "paradise.a.k.y", "35.neco", "hanayama05"]
# arr_parent_username = ["zakkabappy","paradise.a.k.y","35.neco","hanayama05"]


# 2017.10.6
# 2017.10.06 #整理整頓  ★残あり　minmaro_0107　 4,473
# arr_parent_username = ["minmaro_0107"]

# 整理整頓 #クローゼット収納
# arr_parent_username = ["yamazaki.home.channel","yasukichi21","acco.co_m","gemini_natural","lelien_tomo"]
# arr_parent_username = ["acco.co_m","gemini_natural","yasukichi21","lelien_tomo","yamazaki.home.channel"]


# 2017.10.07
# 整理収納　#整理整頓
# arr_parent_username = ["otake_yoko","kurashi___","zuurii1984","pote.pote.pote","syk188","yukitan_home"]
# arr_parent_username = ["kurashi___","zuurii1984","pote.pote.pote","syk188","yukitan_home","otake_yoko"]
# arr_parent_username = ["zuurii1984","pote.pote.pote","otake_yoko","kurashi___","syk188","yukitan_home"]

# 2017.10.09
# イラストレーター
# arr_parent_username = ["maishibasaki","miya78pic","3o_spice","iwatamai"]

# 2017.10.09
# イラストレーター
# arr_parent_username = ["kakashi21gou","ohnuki_fufutime","maishibasaki","miya78pic","iwatamai","3o_spice"]

# 2017.10.10
# ハンドメイドアクセサリー
# arr_parent_username = ["h.a.twinkle.fukuoka","takeme.pw","ohnuki_fufutime","partsclub_official"]

# 2017.10.11
# イラストレーター
# arr_parent_username = ["kakashi21gou", "ohnuki_fufutime", "maishibasaki", "miya78pic", "iwatamai", "3o_spice"]

# 2017.10.12
# 器 #うつわ
# arr_parent_username = ["sumikoaoki", "buchiko1021", "bonmoments_official", "anjicogram", "ouchi_papa", "ouchi_kyoto"]

# 2017.10.13
# 整理収納
# 全入り
# arr_parent_username = ["myhome_yuka_","odayakagurashi","mk.1010","syk188","yukitan_home"]
# arr_parent_username = ["odayakagurashi","mk.1010","syk188","yukitan_home"]

# 2017.10.13
# 整理収納
# arr_parent_username = ["myhome_yuka_", "odayakagurashi", "mk.1010", "syk188", "yukitan_home"]

# 2017.10.16
# フラワーアレンジメント
# arr_parent_username = ["hanajikan_magazine", "rei1008rei", "kolme_tokyo", "mayu_a_a", "mimi.camomille", "sa7ae.h", "ptmd_japan"]

# 2017.10.17
# 紙もの #ペーパーアイテム #ペーパーメッセージ　#ペーパークラフト
# arr_parent_username = ["yuritonari","caramel_miyu","r.a.style","eri.wrapping","jpa0214","chitorinrin","tinklycricket_blog"]

# 2017.10.18
# 節約
# arr_parent_username = ["renyaharutoyuu","mayuuummm","mimimama32502980","cheryl_life"]

# 2017.10.19
# ビール女子
# arr_parent_username = ["beergirl_net","hirokawatae","1megumi36","nomisuke.chan","mamitan.fantasy","rinrinrinco0317","y.318","kida20110321","sumire_ipa1031","rie.k.1023","elly151105","s.ikumi55","kozue_treetop_beer","kuishinboumama"]

# 2017.10.20
# 掃除 #重曹
# arr_parent_username = ["_____mt.hm2","o.remi8900","pyokopyokop","maiotome18"]
# arr_parent_username = ["motegikazuya", "kaori.y.t", "_____mai.3"]

# 2017.10.10
# ハンドメイドアクセサリー  ★残あり   "partsclub_official"  8,929
# arr_parent_username = ["partsclub_official"]

# 2017.10.23
# ハンドメイドアクセサリー　  ★残あり 2,843 "petit_elly","sora_ra_takatora"
# arr_parent_username = ["silver30078","hinatan4442","ayumikitano","petit_elly","sora_ra_takatora"]

# 2017.10.23
# イラストレーター ★残あり　　4,654   "buson2025","rioka_dn"
# arr_parent_username = ["woollydolly","tomokogallery","suesue_99","buson2025","rioka_dn"]

# 2017.10.25
# ほぼ日    残なし
# arr_parent_username = ["jun_hobo","kiri3107","shakemama24","cayodesk","c_quasi","_neconabe_"]

# 2017.10.26
# ハンドメイド小物    ★残あり   884   "ocha.ami"
# arr_parent_username = ["sabumana","hihi731","cokia3884","mamechige","cute211010","clunkystyles","hinatan4442","petitpagu","a_ne_mone.612","btq_official","fujisawananako","mococo.888","niryo1530","ocha.ami"]
# arr_parent_username = ["hihi731","cokia3884","mamechige","cute211010","clunkystyles","hinatan4442","petitpagu","a_ne_mone.612","btq_official","fujisawananako","mococo.888","niryo1530","ocha.ami"]

# 2017.10.27  残なし
# 大桑マイミ @maimiokuwa  #エステティシャン @ayuuu1201  #野沢和香 @wakanozawa 5744
# arr_parent_username = ["maimiokuwa","ayuuu1201","wakanozawa"]
# arr_parent_username = ["maimiokuwa","wakanozawa","yoshikotomioka"]

# 2017.10.30
# セルフネイル    ★残あり　5,351　"mao_gel","canon0k73"　　
# arr_parent_username = ["shiori.o_o.nail","chisato_kukuru","mao_gel","canon0k73"]

# 2017.10.31
# バレエスクール  #バレエ講師　#バレエスタジオ #キッズバレエ    ★残あり 2,342   "mayu09.06","ayame_ystagram"
# arr_parent_username = ["harutakotoe","ballet_school_eclat","hathumi","ebs.2004","tomomi.k07","hiroko_asami","erimuya683","mayu09.06","ayame_ystagram","hathumi"]

# 2017.11.01   残なし
# エステティシャン @ayuuu1201 4,943 + #野沢和香の残で
# arr_parent_username = ["ayuuu1201","harisienne_","purely1","wakanozawa"]

# 2017.11.03  残なし
# 高垣麗子 @reiko___takagaki   #水谷雅子  @mizutanimasako　#美香 @mikaofficial99 #徳澤直子　@tokuzawa.naoko
# arr_parent_username = ["reiko___takagaki","mizutanimasako","mikaofficial99","tokuzawa.naoko"]

# 2017.11.04　#有泉エマ @ema_ariizumi 残なし　　#仁香 @nica77official　は途中でdigを中止（次回digすること）
# 有泉エマ @ema_ariizumi #仁香 @nica77official  #稲沢朋子  @ina_tomo  #五明祐子 @gomyoyuko
# arr_parent_username = ["ema_ariizumi","nica77official","ina_tomo","gomyoyuko"]
# arr_parent_username = ["ema_ariizumi"]

# 2017.11.06
# スタンピンアップ  #カードメイキング #紙もの
# arr_parent_username = ["tatyu5","leafleaf_cards","_emitenten","matsuurasaori","takamisuzukiofficial","nonchan98","mamehan_eri","madame_chin","buno_k","shiho.5128","chikko423","sumiyouko","wonderhouse_official","stampinmasako","tokyostampingirl","ukifuna","sanamuu","maaako0120","fantastica_cat","sealdaijin0719","73candy83"]

# 2017.11.07
# ハンドメイド布小物 #カルトナージュ  #手作り布小物　#手作り雑貨
# arr_parent_username = ["petit_lapin_china_sachi","shibasan48","pitarito_hand","kurumihouse.naoko","tedukuri_my_mama","white_partir","maruishi","clothtasupaper","neige__y"]

# ------------------------------
# 2017.11.6に使うイラストレーター
# ------------------------------
# 2017.10.4
# イラストレーター   ★残あり　"iwashikujira","steven_spielhamburg"  4,845
# arr_parent_username = ["esk.s","illustrator_rikachan","iwashikujira","steven_spielhamburg"]

# 2017.10.09
# イラストレーター   ★残あり　"miya78pic","iwatamai", 1,507
# arr_parent_username = ["kakashi21gou","maishibasaki","miya78pic","iwatamai","3o_spice","ohnuki_fufutime"]

# 2017.10.24　　　
# イラストレーター  ★残あり "buson2025","rioka_dn"　4,654
# arr_parent_username = ["woollydolly","tomokogallery","suesue_99","buson2025","rioka_dn"]
# ------------------------------


# 2017.11.08
# ほぼ日手帳 + イラストレータの残
# arr_parent_username = ["asacoasa","ff310miff","saebonikki"]

# イラストレーター　2017.10.4 2017.10.9 2017.10.24 の残
# arr_parent_username = ["iwashikujira","steven_spielhamburg","miya78pic","iwatamai","buson2025","rioka_dn"]


# 2017.11.09
# 消しゴムはんこ
# arr_parent_username = ["kacoraft","ladymarms_gallery","kyonmush77","73cafe","nana.775","melodyhanko","atelier_naco"]

# 2017.11.10
# 整理収納アドバイザー #収納
# arr_parent_username = ["ito_mikayo", "living_produce", "st.345", "achipetit", "rakuda37", "natsuko2200", "228maco","ayako.anko"]
# 続き
# arr_parent_username = ["yamazaki.home.channel", "otake_yoko", "kurashi___", "yukitan_home"]

# 2017.11.13
# 2017.8.16 ,2017.10.10, 2017.10.23の残　13,271
# ハンドメイドアクセサリー　
# arr_parent_username = ["yossy.toiro","handmade.ale","mofuchibi","petit_elly","sora_ra_takatora","partsclub_official"]

# 2017.11.14
# ハンドメイド #手芸
# arr_parent_username = ["miyuta_ya", "le_bes82", "mokachan.felttoy", "koharubiyori.koharu", "bu_shino77", "r8451","chori_koubow", "toritolion", "framboise_ryoko", "aromama0127", "annie.fukuoka", "ayakoiru"]

# 2017.11.15
# お灸 #お灸堂 #鍼灸サロン(komono.higuchi) #薬草(@_mi.ho._ から @jamha_herblifeまで) #ナチュラル化粧品 (@botanicanon_jp〜@hitomi.morimoto) #温活   @megumi_kanzaki  神崎恵 の残   #仁香 @nica77official　
# arr_parent_username = ["sennenq_beauty","sennenq_kyoto","sennenq_osaka","sennenq.ginza","okyudo","komono.higuchi","_mi.ho._","kunihiro_takei","haruyo8takayama","jamha_herblife","botanicanon_jp","momobeaute_in_germany","hitomi.morimoto","sakufinity","scheinen","megumi_kanzaki","nica77official"]
# arr_parent_username = ["sennenq_beauty","sennenq_kyoto","sennenq_osaka","sennenq.ginza","okyudo","komono.higuchi","_mi.ho._","kunihiro_takei","haruyo8takayama","jamha_herblife","botanicanon_jp","momobeaute_in_germany","hitomi.morimoto","sakufinity","scheinen"]

# 2017.11.16  #鍼灸院  #鍼灸サロン
arr_parent_username = ["botanicanon_jp", "momobeaute_in_germany", "hitomi.morimoto", "sakufinity", "scheinen","komono.hari", "komono.sakae", "ginza_haricchi", "shinkyusalon_komachi"]

# 2017.11.17
# 整理収納
# arr_parent_username = ["sakibus01","saori.612","kozu_tani_inside","cherryleaf0915","miii1123","flow_hayuka","maaaako_home","gomarimomo"]

# -------------------------------------
# main process
# -------------------------------------

conn = MySQLdb.connect(db='insta_like', user='python_usr', passwd='admin@python', charset='utf8mb4')
cur_mysql = conn.cursor()  # カーソルを取得する。

int_total_target_user_cnt = 0

for parent_username in arr_parent_username:

    # -------------------------------------
    # 親ユーザーページの情報をmst_parent_userへ格納
    # -------------------------------------
    try:
        str_sql = "SELECT uno, user_id, input_date, update_date FROM mst_parent_user WHERE user_id = %s "

        cur_mysql.execute(str_sql, (parent_username,))
        result = cur_mysql.fetchall()

        # mst_parent_userにparent_usernameが登録済み
        if len(result) > 0:

            str_msg = ">>" + parent_username + "(" + str(result[0][0]) + ")"
            print(str_msg)
            str_msg = " - 登録済 (登録日:" + str(result[0][2].strftime('%Y-%m-%d'))

            if str(result[0][3]) != "None":
                str_msg = str_msg + " 更新日：" + str(result[0][3].strftime('%Y-%m-%d')) + ")"
            else:
                str_msg = str_msg + ")"

            print(str_msg)

            # 子ユーザーの登録件数
            str_sql = "SELECT count(*) FROM tbl_follow_user WHERE parent_uno = %s "
            cur_mysql.execute(str_sql, (str(result[0][0]),))
            result_all = cur_mysql.fetchall()

            str_msg1 = "登録フォロワー数:" + str(result_all[0][0])

            # 子ユーザーのいいね対象件数
            str_sql = "SELECT count(*) FROM tbl_follow_user WHERE parent_uno = %s  and trg_flg = 1 and on_mark IS NULL"
            cur_mysql.execute(str_sql, (str(result[0][0]),))
            result_on = cur_mysql.fetchall()
            str_msg2 = "いいね対象数:" + str(result_on[0][0])

            # 子ユーザーの対象外件数
            str_sql = "SELECT count(*) FROM tbl_follow_user WHERE parent_uno = %s  and trg_flg = 0 "
            cur_mysql.execute(str_sql, (str(result[0][0]),))
            result_off = cur_mysql.fetchall()
            str_msg3 = "いいね対象外数:" + str(result_off[0][0])

            print(" - " + str_msg1 + "  " + str_msg2 + "  " + str_msg3)
            print("")

            int_total_target_user_cnt += result_on[0][0]

        # mst_parent_userにparent_usernameが未登録
        else:
            print(">>" + parent_username + "　は未登録です。")
            print("")

    except Exception as e:
        conn.close()  # コネクションを閉じる。
        print(traceback.format_exc())

str_end_msg = "総対象者数: " + "{:,}".format(int_total_target_user_cnt)
# print ("総対象者数: " + "{:,}".format(int_total_target_user_cnt))
print(str_end_msg)
conn.close()  # コネクションを閉じる。
