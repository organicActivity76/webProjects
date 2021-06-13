from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 26

anime_db = [
    {
        'id': 1,
        'title': 'anime',
        'def': 'Japanese word for cartoon and animation. In Japan, "anime" refers to any and all animation or cartoon - regardless of the genre, style, or nation of origin. Outside of Japan the word "anime" has come to refer specifically to animation of Japanese origins, or animation of a particular.<br><br> Defined by origin: Defining "anime" as animation produced in Japan allows for a fairly black and white application of the label. The only gray area occurs with co-productions that may have had a portion of their animation, and/or scripting produced outside of Japan.<br><br>Defined by style: Defining "anime" as a style of animation that originated in Japan is much more complicated, however this definition would allow animation produced outside of Japan, but conforming to the defined "style" to be called "anime." It is difficult to determine if this "style" should be determined solely on drawing style (ie: Big eyes, small mouth, pointy hair), if it should include editing techniques (Japanese animation typically makes more use of "cuts" and "camera angles" than most non Japanese animation), and whether the narrative or storytelling style should be included in the definition. Perhaps the biggest pitfall of this definition is that, due to the wide variety of Japanese animation, regardless of any style based definition, there will always be Japanese animation that would not fit the definition, creating a scenario where some Japanese animation would not be anime.',
        'img': ['https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/12/Crunchyroll-most-watched-anime-header.jpg','https://static0.srcdn.com/wordpress/wp-content/uploads/2019/12/A-couple-of-the-decades-most-popular-anime.jpg']
    },
   {
        'id': 2,
        'title': 'cosplay',
        'def': 'Cosplay is a term that originated in Japan but is based on the English words "Costume Play", essentially play-acting in costumes.<br><br>In Japan Cosplay is not limited to anime/manga, but also a staple of many other entertainment industries such as science fiction and horror. In North America the term Cosplay is reserved for anime/manga related costuming.<br><br>Cosplaying can be divided into two categories: basic cosplay and Masquerade. While basic cosplay only involves an attempt to look like a particular character, either in the halls of a convention or on stage, Masquerade is much more involved. When Masquerading, cosplayers attempt to act as the character would. They often have prepared skits with memorized lines, and the more advanced masqueraders can easilly ad-lib their character\'s personality.',
        'img': ['https://dw9to29mmj727.cloudfront.net/promo/2016/5257-SeriesHeaders_SMv3_2000x800.jpg','https://static2.srcdn.com/wordpress/wp-content/uploads/2019/04/Sailor-Scouts-Sailor-Moon-Cosplay-e1554743216281.jpg?q=50&fit=crop&w=740&h=397']
    },
    {
        'id': 3,
        'title': 'cours',
        'def': 'A measurement of the length of a television series. A one-season series (of generally 13 weekly episodes) is described as being "one cours" long, while a two-season series (of generally 26 episodes) would be described as "two-cours." <br><br>Although generally 13 episodes, the exact number of episodes in a cours can vary. It is often between 11 and 14 episodes, with 13 episodes being the most common count.',
        'img': ['https://i1.wp.com/anitrendz.net/news/wp-content/uploads/2019/08/Testing_1.png?fit=1200%2C675&ssl=1','https://i.imgur.com/Z4VuNpa.jpg?1']
    },
    {
        'id': 4,
        'title': 'doujin',
        'def': 'Doujin is short for Dōjinshi and in conversation people usually will say doujin. Dōjinshi manga are non-professional and/or self published comics, and dōujin refers to any self-published work. Dōjinshi manga can be broken into two broad categories: fan-comics and original works. Fan-comics, much like fan-fiction, are based on established properties and created by fans of those properties. Original works are based on the dōjinshi-ka\'s (creator) original ideas. The only difference between mainstream manga and original dōjinshi is that the dōjinshi is not published by a publishing company; it is self-published by the dōjinshi-ka.<br><br>Dōjinshi is essentially amateur comic publishing, but not all dōjinshi-ka are amateurs. Many professional, published artists continue to self-publish dōjinshi in addition to their mainstream manga. These dōjinshi may be new original works that they chose not to (or are unable to) have published by a larger company. They can also be side-stories that the artists create for fans of their published works.',
        'img': ['https://imgcp.aacdn.jp/img-a/1200/900/global-aaj-front/article/2017/02/58afb2a0ad2f6_58afaf9081c38_587948920.jpg','https://img.mipon.org/wp-content/uploads/2018/11/04034133/Saint-Seiya_doujinshi_Comiket.jpg']
    },
    {
        'id': 5,
        'title': 'dub',
        'def': 'When voice recordings and sound effects are added to animation, this process is called dubbing. In anime, both the original Japanese audio and the localized English audio are technically dubs.<br><br>However in anime, and other forms of international cinema, fans have come to refer to the translated material as dubbed. In this sense, a non-official (non-correct) accepted definition for dub is:<br><br>v. to dub / dubbing <br><br>Recording of a translated vocal track and replacing the original vocal track with the translated one. <br><br>n. dub<br><br>A video (movie, tv series, etc...) where the original language vocal track has been replaced with a recorded translation.',
        'img': ['https://pm1.narvii.com/5946/a69038d3bd556978de69d61e859b05ab3cefa3c8_hq.jpg','https://pm1.narvii.com/5946/4cd3b0de150b0c43a6f81203749cf4cf4ef50636_hq.jpg']
    },
    {
        'id': 6,
        'title': 'husbando',
        'def': 'A male anime or video game character that one considers as their husband or lover.',
        'img': ['https://i2.wp.com/animecrackerz.com/wp-content/uploads/todoroki-cutest-anime-husbando-2019.jpg?w=700&ssl=1','https://i0.wp.com/animecrackerz.com/wp-content/uploads/levi-ackerman-cutest-anime-husbando-2019.jpg?w=700&ssl=1']
    },
    {
        'id': 7,
        'title': 'isekai',
        'def': 'A subgenre of Japanese light novels, manga, anime, and video games. Isekai works revolve around a normal person from Earth being transported to, reborn, or trapped in a parallel universe, usually a fantasy world. Often, the protagonist is already familiar with the parallel world, as it is often a fictional universe from a fictitious work published in the protagonist\'s origin universe, but the parallel world may also be unknown to them',
        'img': ['https://images-na.ssl-images-amazon.com/images/I/91Aw3hzm5QL._RI_.jpg','https://akibento.com/blog/wp-content/uploads/2017/11/f232bb1b8ce331eedca40442dd30a26b129feee4_hq.jpg']
    },
    {
        'id': 8,
        'title': 'in-between',
        'def': 'Once the key frames of an animation are created, junior level artists (sometimes at a different studio in another country) go in and add frames between the key frames to make the motion smoother - hence the name in-betweens (or tweens for short). These are often looser and less on model since they just help move from one important key frame to another and also due to the lower skill level of those junior animators.<br><br>In-betweening is widely regarded as drudge work in the animation industry. This is where inexperienced animators begin their career but it is repetitive, uncreative work, and the inbetweeners often have extremely high production quotas to be met. In-betweening is often subcontracted to the lowest bidder, which can result in shoddy work.',
        'img': ['https://cdn.myanimelist.net/s/common/uploaded_files/1506998654-4e13c2eab84db588cdeb03b9a0b0e8d7.png','https://i.imgur.com/3GCO1af.gif']
    },
    {
        'id': 9,
        'title': 'josei',
        'def': 'Demographic indicator for anime and manga aimed at women. One of the rarest forms of anime, a significant proportion of josei anime/manga appears to fall under the category of "yaoi." Although there are some housewife/family/young mother stories in manga format in Japan, non-yaoi josei is relatively underpublicized in the West. Popular examples of non-yaoi josei include Paradise Kiss and Honey and Clover.',
        'img': ['https://66.media.tumblr.com/tumblr_lyodiuYytm1rnoqhoo1_500.gifv','https://nefariousreviews.files.wordpress.com/2017/03/honey-and-clover-featured.jpg']
    },
    {
        'id': 10,
        'title': 'magical girl',
        'def': 'A subgenre of Japanese fantasy light novels, manga, anime, and video games which features girls who use magic or possess magical powers. Magical girls transform to unlock their powers and are often accompanied by an animal mascot, using wands or scepters as a weapon to fight monsters and the forces of evil.',
        'img': ['https://vignette.wikia.nocookie.net/prettycure/images/7/73/GPPC_Vocal_Album_1.jpg/revision/latest?cb=20151113115326','https://animemotivation.com/wp-content/uploads/2017/02/madoka-magica-quotes.jpg']
    },
    {
        'id': 11,
        'title': 'manga',
        'def': 'In Japan the word manga refers to all forms of comics, be they Japanese, European or American. But in Europe and America the word manga is used to refer specifically to Japanese comics.<br><br>The Japanese anime industry is a spin-off of the manga industry. This explains in part the difference between Japanese and Western animation. In Japan animation is considered as a "moving manga", whereas in Europe and North America it is considered as a "drawn movie", with all the expectations that this entails. Originally most anime was based on already existing and successful manga, however in recent years leaps in the Japanese animation industry have led to manga being based on successful original anime.',
        'img': ['https://i.pinimg.com/originals/bc/87/59/bc8759d34cf7d43c0adcf87120786d51.jpg','https://www.rightstufanime.com/images/productImages/9781569319208_manga-Dragon-Ball-1-sample4.jpg']
    },
    {
        'id': 12,
        'title': 'manhwa',
        'def': 'Manhwa (만화) is the Korean equivalent to manga and is the Korean term used to describe comics. As with the Japanese term, when used in Korean, Manhwa is used to refer to comics of all origins, however when it is used in English, manhwa is used exclusively to refer to comics of Korean origin.',
        'img': ['https://i.pinimg.com/736x/e7/96/e2/e796e25b731a1a93ae454f1743d65c20.jpg','https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/02/CBR-Featured-Image-Best-Romance-Manwha.jpg']
    },
    {
        'id': 13,
        'title': 'mecha',
        'def': 'Short for "mechanical," mecha has two different meanings in Japanese and English. <br><br>In Japanese, the term is used to refer to anything mechanical from robots and spacecraft to bicycles and toasters. The robots in Mobile Suit Gundam are mecha in Japanese, and so are the cars in You\'re Under Arrest. Some English-speaking fans have repurposed the term to only mean piloted or controlled robots. The variable fighters from Macross and mobile suits from Gundams are prominent examples of mecha in this redefined version of the term.',
        'img': ['https://manga.tokyo/wp-content/uploads/2016/12/gundam.jpg','https://img1.ak.crunchyroll.com/i/spire4/34f4fc621d599150ec9a069149e6c5b71539517181_full.jpg']
    },
    {
        'id': 14,
        'title': 'moe',
        'def': 'Moe is a Japanese term used in connection with manga or anime to describe something precious, usually (but not always) the ideal of youthful and innocent femininity. Written with the kanji for "to bud or sprout" (萌), the concept covers a range of ideal behaviour for youthful female characters in manga or anime.<br> To be moe, a character can be eager or perky, not overly independent, and call forth a desire in the viewer to protect them and nurture them.',
        'img': ['https://i.ytimg.com/vi/E1x1RicXFMk/maxresdefault.jpg','https://media1.giphy.com/media/tZisK9dZ3JGa4/source.gif']
    },
    {
        'id': 15,
        'title': 'otaku',
        'def': 'Means geek, nerd, enthusiast. It can also mean hardcore anime/manga or hardcore fans of any hobby',
        'img': ['https://i.pinimg.com/originals/30/e6/0f/30e60f7c118457d2c6ecc5513f1830d6.jpg','https://i.pinimg.com/originals/a2/ab/d4/a2abd4c92fb642588edfb5ea9745e30e.jpg']
    },
    {
        'id': 16,
        'title': 'seinen',
        'def': 'Relatively uncommon in the west due to the emphasis on the male teen market, "seinen" is a demographic indicator for anime and manga aimed at a young adult male (college-aged) audience. As such, this kind of anime tends to be more sophisticated than shōnen anime. There are many of the same basic themes/subgenres as shōnen but they are more psychological, satirical, violent, sexual, etc. In other words they are intended for a more mature audience.Overall, seinen anime tends to be more strongly rooted in reality, with many incidental details added to heighten the sense of realism and even fantasy elements being subject to a strong "realistic" logic. Of course, it should be noted that those stylistic guidelines are a generalization of the genre and even an anime that has none of those characteristics can be classified as seinen if that was indeed the target audience. In fact, hentai (not including yaoi) is mostly targeted at the seinen demographic.',
        'img': ['https://images-na.ssl-images-amazon.com/images/I/71zMifmAR0L.jpg','https://www.anime-planet.com/images/anime/covers/kaiji-against-all-rules-3756.jpg']
    },
    {
        'id': 17,
        'title': 'simulcast',
        'def': 'Refers to anime that are simultaneously broadcast in on television in Japan and over the Internet in international markets. This is actually a slight misnomer as very few of these anime titles are actually streamed online at the exact same time as they are aired in Japan. The term simulcast has come to be used for shows that are streamed online within approximately 24 hours of the original Japanese broadcast, however it has been used on occasion for shows streamed several days after the original broadcast.',
        'img': ['https://res.cloudinary.com/sfp/image/upload/q_60/cste/1d84d860-4582-41ad-937d-b5ceb18c739e.jpg','https://image.myanimelist.net/ui/5LYzTBVoS196gvYvw3zjwBiwKJg2-TVIvTts4YFbaVg']
    },
 
    {
        'id': 18,
        'title': 'seiyu',
        'def': 'Seiyū is the Japanese term for voice actor or actress - whether in animation, radio, dubbed non-Japanese films, etc. In Japan, seiyū are often less anonymous as artists than voice actors in the West. Many of the most famous seiyū (e.g. Megumi Hayashibara) have large fan groups of their own.',
        'img': ['https://i.pinimg.com/originals/4d/de/d2/4dded29f7a68176f2c8b4fe3160cedac.jpg','https://i.ytimg.com/vi/iHwnXybl5kY/maxresdefault.jpg']
    },
    {
        'id': 19,
        'title': 'senpai',
        'def': 'Japanese term used to refer to one\'s elder in an organization. Most commonly used in school and at work to refer to a person with more seniority than the speaker. For example a first grader would call anyone in second grade or higher "senpai."<br><br>Senpai can be used as a title (example: "Good day senpai") or as an honorific (example "Ogata-senpai) will be leaving soon." Most often the pronoun form is used when directly addressing the senior, while the honorific is used when referring to him (or her) in conversation with a third party.',
        'img': ['https://cdn2.scratch.mit.edu/get_image/gallery/4863437_170x100.png','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTku2nI-rB7gWk1QqGLoMu_msWn2Gs14p4UvnjbQ5kAAidWxVWv&s']
    },
    {
        'id': 20,
        'title': 'shojo',
        'def': '"Shōjo" is a demographic indicator for anime and manga aimed at girls. However, among Western fans, it is often misinterpreted to mean "an anime with the stylistic qualities usually associated with shōjo". In other words, shōjo is associated with a visual and storytelling style rather than with a demographic. While it is true that shōjo anime and manga traditionally tend to have a strong focus on relationships and character development, it is far too diverse to be pigeonholed so neatly. Weiss Kreuz, for example, could at first glance be mistaken for a shōnen anime with its good guys fighting bad guys. But the emphasis on bishōnen (as well as the hordes of female fans) make it clear that this is an anime aimed at girls, and therefore shōjo. And while some shōjo can be totally devoid of any true antagonism, other will feature soul-blithering drama.<br><br>There is a popular subgenre of shōjo called mahō shōjo, or "magical girl". While there are many subgenres of shōjo, this one is predominant enough to warrant a special mention. In said subgenre the heroines receive magical powers, usually for the purpose of fighting evil in the name of love and justice. Elaborate transformation sequences and cute costumes are a staple of magical girls. This subgenre also tends to feature more action than traditional shōjo.',
        'img': ['https://geeksoncoffee.com/wp-content/uploads/2020/01/Best-Shoujo-Anime-of-All-Time.jpg','https://i1.wp.com/skdesu.com/wp-content/uploads/2017/02/romance-kawaii.jpg?w=1200&ssl=1']
    },
    {
        'id': 21,
        'title': 'shonen',
        'def': 'Demographic indicator for anime and manga aimed at boys. An obvious and common example of shōnen is "fighting" anime, where extremely powerful warriors duke it out amongst each other with various forms of martial arts and superpowers. Typical examples of this include Dragon Ball Z, Flame of Recca and Rurouni Kenshin.<br><br>Despite a great increase in sophistication through the years, may shōnen anime remains largely centered on the resolution of conflicts through combat. However, that is not to say this is the only thing. If nothing else, this is proven by the large quantity of romantic comedy "harem" anime where a large cast of attractive females are vying for the attention of the (indecisive) male protagonist, like Tenchi Muyo! and Love Hina. Other examples of non-fighting shōnen anime are the sports anime like Slam Dunk that are starting to make an impact in the West.<br><br>Besides violence or combat, one characteristic of many shōnen anime is a fast-paced story where action and adrenalin are emphasized over plot. There are exceptions to this, like the romantic stories of I''s and Boys Be...',
        'img': ['https://usercontent2.hubstatic.com/13152011_f1024.jpg','https://techlapse.com/wp-content/uploads/2019/07/Anime-2K19-techlapse-1200x900.png']
    },
    {
        'id': 22,
        'title': 'sub',
        'def': '"Sub anime" is short for "subtitled anime". That is Japanese animated movies or TV shows presented with the original Japanese spoken dialogue, but with subtitles translating the dialogue into another language',
        'img': ['https://media1.giphy.com/media/apTHUosHGIBLG/source.gif','https://i.imgur.com/RGcM2q9.jpg']
    },
    {
        'id': 23,
        'title': 'tsundere',
        'def': 'A character who starts off cold and indifferent until you get to know them, then find their warm and gooey center.',
        'img': ['https://i.kym-cdn.com/photos/images/original/000/169/215/Tsunderekko.jpg','https://img1.ak.crunchyroll.com/i/spire3/bb2f97f9e6f5b4712f1ff8ce7f5b63061405740316_full.jpg']
    },
    {
        'id': 24,
        'title': 'waifu',
        'def': ' A fictional character from non-live-action visual media (typically an anime, manga, or video game) that one is attracted to and considers a significant other.',
        'img': ['https://media.tenor.com/images/d5322e1b25dd34b71714862338932f3f/tenor.gif','https://i.ytimg.com/vi/WV0c2F--59A/maxresdefault.jpg']
    },
    {
        'id': 25,
        'title': 'yaoi',
        'def': 'Yaoi, also known as boy\'s love or BL, is a genre of fictional media originating in Japan that features homoerotic relationships between male characters. It is typically created by women for women and is distinct from homoerotic media marketed to gay and bisexual male audiences, such as bara, but it can also attract male readers and male creators can also produce it. It spans a wide range of media, including manga, anime, drama CDs, novels, games, and fan production. Boys love and its abbreviation BL are the generic terms for this kind of media in Japan and have, in recent years, become more commonly used in English as well. However, yaoi remains more generally prevalent in English. ',
        'img': ['https://i1.wp.com/recommendmeanime.com/wp-content/uploads/2016/07/super-lover-romance.jpg?fit=1024%2C545&ssl=1&resize=1280%2C720','https://i0.wp.com/recommendmeanime.com/wp-content/uploads/2017/11/Hitorijime-My-Hero-anime.jpg?fit=1024%2C577&ssl=1']
    },
    {
        'id': 26,
        'title': 'yuri',
        'def': 'A genre involving lesbian relationships or female homoeroticism in light novels, manga, anime, video games and related Japanese media.[4][5] Yuri focuses on the sexual orientation or the romantic orientation aspects of the relationship, or both',
        'img': ['https://static0.cbrimages.com/wordpress/wp-content/uploads/2020/02/Best-Yuri-Anime-of-the-2010s.jpg','https://static2.cbrimages.com/wordpress/wp-content/uploads/2020/02/Bloom-Into-You.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5']
    },


]

score = 0


@app.route('/')
def home_page():
    return render_template('home.html', anime_db=anime_db)  

@app.route('/view/<id>', methods=['GET', 'POST'])
def anime(id=None):

    anime_id = int(id)
    
    anime_index = None
    for (i,a) in enumerate(anime_db):
        a_id = a['id'] 
        if a_id == anime_id:
            anime_index = i

    animeTerm = anime_db[anime_index]

    return render_template('animeTerm.html', anime_db=anime_db, animeTerm=animeTerm)

@app.route('/search/<search_query>', methods=['GET', 'POST'])
def search(search_query=None):
    
    searchQuery = search_query

    return render_template('search.html', anime_db=anime_db, searchQuery=searchQuery)

@app.route('/create')
def create_anime():
    return render_template('create.html') 

@app.route('/easy_q1')
def easy_q1():
    return render_template('easy_q1.html', anime_db=anime_db)

@app.route('/easy_q2')
def easy_q2():
    return render_template('easy_q2.html', anime_db=anime_db)

@app.route('/easy_q3')
def easy_q3():
    return render_template('easy_q3.html', anime_db=anime_db)

@app.route('/easy_q4')
def easy_q4():
    return render_template('easy_q4.html', anime_db=anime_db)

@app.route('/easy_q5')
def easy_q5():
    return render_template('easy_q5.html', anime_db=anime_db)

@app.route('/med_q1')
def med_q1():
    return render_template('med_q1.html', anime_db=anime_db)

@app.route('/med_q2')
def med_q2():
    return render_template('med_q2.html', anime_db=anime_db)

@app.route('/med_q3')
def med_q3():
    return render_template('med_q3.html', anime_db=anime_db)

@app.route('/med_q4')
def med_q4():
    return render_template('med_q4.html', anime_db=anime_db)

@app.route('/med_q5')
def med_q5():
    return render_template('med_q5.html', anime_db=anime_db)

@app.route('/hard_q1')
def hard_q1():
    return render_template('hard_q1.html', anime_db=anime_db)

@app.route('/hard_q2')
def hard_q2():
    return render_template('hard_q2.html', anime_db=anime_db)

@app.route('/hard_q3')
def hard_q3():
    return render_template('hard_q3.html', anime_db=anime_db)

@app.route('/hard_q4')
def hard_q4():
    return render_template('hard_q4.html', anime_db=anime_db)

@app.route('/hard_q5')
def hard_q5():
    return render_template('hard_q5.html', anime_db=anime_db)



@app.route('/quiz_results')
def quizResults():
    return render_template('quiz_results.html', anime_db=anime_db, score=score)

@app.route('/increase_score', methods=['GET','POST'])
def increaseScore():
    global score
    score += 1
    return jsonify(score=score)

@app.route('/reset_score', methods=['GET','POST'])
def resetScore():
    global score
    score = 0
    return jsonify(score=score)

@app.route('/save_entry', methods=['GET', 'POST'])
def save_entry():
    global anime_db 
    global current_id

    #UPDATES ANIME DB 
    new_anime_data = request.get_json()
    new_anime_data['id'] = current_id
    current_id += 1
    anime_db.append(new_anime_data)

    return jsonify(new_anime_data = new_anime_data)

@app.route('/submit_title', methods=['GET', 'POST'])
def submit_entry():
    global anime_db 
    
    animeToChange = request.get_json()
    changedName = animeToChange['title']  
    animeID = int(animeToChange['id'])
    print(changedName)
    print(animeID)

    #find the anime with this id and change the title
    index_to_change = None
    for (i, a) in enumerate(anime_db):
        a_id = a['id']
        if a_id == animeID:
            index_to_change = i

    if index_to_change is not None:
        anime_entry = anime_db[index_to_change]
        anime_entry['title'] = changedName
        #anime_db[index_to_change].title = changedName

    return jsonify(changedName = changedName)



if __name__ == '__main__':
   app.run(debug = True)




