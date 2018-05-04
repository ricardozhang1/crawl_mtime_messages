#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json

class HtmlParser(object):

    def parser_url(self,page_url,response):
        pattern = re.compile(r'http://movie.mtime.com/(\d+)/')
        urls = pattern.findall(response)
        if urls != None:
            #去重url
            return list(set(urls))
        else:
            return None


    def parser_json(self,page_url,response):
        pattern = re.compile(r'=(.*?);')
        result = pattern.findall(response)[0]
        if result != None:
            value = json.loads(result)
            try:
                isRelease = value.get('value').get('isRelaase')
            except Exception as e:
                print(e)
                return None
            if isRelease:
                if value.get('value').get('hotValue') == None:
                    return self._parser_release(page_url, value)
                else:
                    return self._parser_no_release(page_url,value,isRelease=2)
            else:
                return self._parser_no_release(page_url,value)


    def _parser_release(self,page_url,value):
        try:
            isRelease = 1
            movieRating = value.get('value').get('movieRating')
            boxOffice = value.get('value').get('boxOffice')

            movieTitle = value.get('value').get('movieTitle')
            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')

            TotalBoxOffice = boxOffice.get('TotaBoxOffice')
            TotalBoxOfficeUnit = boxOffice.get('TotalboxUnit')
            TodayBoxOffice = boxOffice.get('TodayBoxOffice')
            TodaylBoxOfficeUnit = boxOffice('TodayBoxOfficeUnit')
            ShowDays = boxOffice.get('ShowDays')
            try:
                Rank = boxOffice.get('Rank')
            except Exception as e:
                Rank = 0
            return (MovieId,movieTitle,RatingFinal,ROtherFinal,RPictureFinal,RDirectorFinal,RStoryFinal,Usercount,AttitudeCount,TotalBoxOffice+TotalBoxOfficeUnit,TodayBoxOffice+TodayBoxOffice+TodaylBoxOfficeUnit,Rank,ShowDays,isRelease)
        except Exception as e:
            print(e,value)
            return None


    def _parser_no_release(self,page_url,value,isRelease=0):
        try:
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')
            try:
                Rank = value.get('value').get('hotValue').get('Ranking')
            except Exception as e:
                Rank = 0
            return (MovieId,movieTitle,RatingFinal,ROtherFinal,RPictureFinal,RDirectorFinal,RStoryFinal,Usercount,AttitudeCount,u'无',u'无',Rank,0,isRelease)
        except Exception as e:
            print(e,value)
            return None








if __name__ == '__main__':
    r = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head>    <title>厦门影讯,厦门电影院-在线选座购票-购电影票</title>         <meta name="Keywords" content="电影院,优惠,购票,电影票,影城,厦门电影院,厦门影讯" />    <meta name="Description" content="时光网电影院频道提供厦门电影院影讯查询及在线选座购票服务,可以查到后来的我们,幕后玩家放映时间,排片,电影票价,以及各电影院电影排期,地址电话地图信息" />    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<link type="image/x-icon" href="http://static1.mtime.cn/favicon.ico" rel="icon"/>
<link type="image/x-icon" href="http://static1.mtime.cn/favicon.ico" rel="shortcut icon"/>
<link type="image/x-icon" href="http://static1.mtime.cn/favicon.ico" rel="bookmark"/>
<link type="application/opensearchdescription+xml" href="http://feed.mtime.com/opensearch.xml" title="Mtime影视搜索" rel="search" />
<link rel="alternate" type="application/rss+xml" title="影评" href="http://feed.mtime.com/comment.rss"/>
<link rel="alternate" type="application/rss+xml" title="日志" href="http://feed.mtime.com/blog.rss"/>
<link rel="alternate" type="application/rss+xml" title="资讯" href="http://feed.mtime.com/news.rss"/>
<link rel="alternate" type="application/rss+xml" title="话题" href="http://feed.mtime.com/topic.rss"/>
<link rel="alternate" type="application/rss+xml" title="周刊" href="http://feed.mtime.com/weekly.rss"/>
<script type="text/javascript">
  var server = "http://static1.mtime.cn/";
  var subServer = "http://static1.mtime.cn/theater/";
  var version = "20180308112746";
  var subVersion = "20180306104347";
  var jsServer = server + version;
  var cssServer = server + version;
  var subJsServer = subServer + subVersion;
  var subCssServer = subServer + subVersion;
  var debug = false;
  var mtimeCookieDomain = "mtime.com";
  var siteLogUrl = "http://log.mtime.cn";
  var siteServiceUrl = "http://service.mtime.com";
  var siteTheaterServiceUrl = "http://service.theater.mtime.com";
  var crossDomainUpload="http://upload3.mtime.com/Upload.ashx";
</script>
<script type="text/javascript">
  document.write(unescape("%3Clink href='" + cssServer + "/css/2014/publicpack.css' rel='stylesheet' media='all' type='text/css'%3E%3C/link%3E"));
</script>
<script type="text/javascript">
	document.write(unescape("%3Clink href='" + subCssServer + "/css/cinema.css' rel='stylesheet' media='all' type='text/css'%3E%3C/link%3E"));
</script>
</head><body pn="M14_TheaterIndex">	<script type="text/javascript">
	var navigationBarType = 1;document.writeln( "<div id=\"topbar\"></div>");var debug = false;var mtimeCookieDomain="mtime.com";var siteLogUrl="http://log.mtime.cn";var siteUrl="http://www.mtime.com";var siteMcUrl="http://my.mtime.com";var siteApiUrl="http://api.mtime.com";var siteBlogUrl="http://i.mtime.com";var siteGroupUrl="http://group.mtime.com";var siteMovieUrl="http://movie.mtime.com";var sitePeopleUrl="http://people.mtime.com";var siteNewsUrl="http://news.mtime.com";var siteServiceUrl="http://service.mtime.com";var siteSearchUrl="http://search.mtime.com";var siteGoodsListUrl="http://list.mall.mtime.com";var theaterService="http://service.theater.mtime.com";var siteLibraryServiceUrl="http://service.library.mtime.com";var siteCommunityServiceUrl="http://service.community.mtime.com";var siteChannelServiceUrl="http://service.channel.mtime.com";var siteGoodsServiceUrl="http://service.mall.mtime.com";var siteTradeServiceUrl="http://trade.mtime.com";var siteFunUrl="";var sitePassportUrl="http://passport.mtime.com";var crossDomainUpload="http://upload3.mtime.com/Upload.ashx";var topMenuValues={"searchTip":"烈火战车","bgUrl":"http://movie.mtime.com/10910/","bgSrc":"http://img31.mtime.cn/mg/2016/05/13/174333.71622876.jpg","bgStartDate":new Date("May, 15 2016 00:00:00"),"bgEndDate":new Date("May, 15 2016 00:00:00"),"logoBGColor":"","bgHeight":0,"mainNavType":"Channel","footer":"<dt class=\"clearfix\"><span class=\"fr\">第209期</span><strong>时光周刊</strong></dt>\n                <dd><a href=\"http://www.mtime.com/weekly/\" target=\"_blank\" title=\"时光周刊\"><img src=\"http://img5.mtime.cn/mg/2018/04/13/164158.36123877.jpg\" width=\"170\" alt=\"时光周刊\"></a></dd>"};
</script>
<div id="headImgDiv" class="i_newshead">
    
    <a href="#" id="headImgPre" class="lastnews" title="上一篇"><i></i></a>
    <a href="#" id="headImgNext" class="nextnews" title="下一篇"><i></i></a>
    
    <ul id="headImgBackSlidesRegion" class="bgimg">
    	<li style="background-image:url(http://img5.mtime.cn/mg/2018/04/28/093805.44580932.jpg);opacity:1;z-index:2;background-repeat:no-repeat;" class="transition3"></li>
    	<li style="background-image:url(http://img5.mtime.cn/mg/2018/04/10/155600.65759564.jpg);opacity:0;z-index:1;background-repeat:no-repeat;" class="transition3"></li>
    </ul>
    
    <div id="headImgDotSlidesRegion" class="i_newsnav">
    	<a href="#" class="on" onclick="return false;">1</a>
        <a href="#" onclick="return false;">2</a>    
    </div>
    <div class="i_newsimgs">
        <div class="dl">
            <div id="headImgTxtSlidesRegion" class="i_newstitbox">
                <div class="textbox transition4 transition6 __r_c_" style="opacity:1;display:block;" pan="M14_TheaterIndex_HeadImg1">
                    <span class="hotfilm">正在热映</span>
                    <h2><a href="http://movie.mtime.com/233465/" target="_blank" style="">《幕后玩家》</a></h2>
                    <p class="textinfo">114分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank" style="">剧情</a><span mid="233465" method="hotplay"></span></p>
                    <p class="textinfo"><i class="ico_ydot"></i><a href="http://movie.mtime.com/233465/" target="_blank" style="">徐峥被困密室面临生死抉择</a></p>
                    <p class="morelink"><a href="http://movie.mtime.com/233465/" target="_blank" style=""><span class="icon-add"><em>+</em></span>查看详情</a></p>
                </div>
                <div class="textbox transition4 transition6 __r_c_" style="opacity:0;display:none;" pan="M14_TheaterIndex_HeadImg2">
                    <span class="hotfilm">正在热映</span>
                    <h2><a href="http://movie.mtime.com/225925/" target="_blank" style="">《狂暴巨兽》</a></h2>
                    <p class="textinfo">108分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank" style="">动作</a>/<a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank" style="">冒险</a><span mid="225925" method="hotplay"></span></p>
                    <p class="textinfo"><i class="ico_ydot"></i><a href="http://movie.mtime.com/225925/" target="_blank" style="">强森带领"拯救世界小队"逆袭巨兽</a></p>
                    <p class="morelink"><a href="http://movie.mtime.com/225925/" target="_blank" style=""><span class="icon-add"><em>+</em></span>查看详情</a></p>
                </div>
            </div>
            
            <dl id="headImgSlidesRegion" class="clearfix">
                <dd style="opacity:1;z-index:2;" class="transition8 __r_c_" pan="M14_TheaterIndex_HeadImg1">
                    <h2>《幕后玩家》</h2>
                    <a href="http://movie.mtime.com/233465/" title="《幕后玩家》" target="_blank"><img src="http://img5.mtime.cn/mg/2018/04/28/093759.73655143.jpg" width="1000" height="390" alt="《幕后玩家》" /></a>
                </dd>
                <dd style="opacity:0;z-index:1;" class="transition8 __r_c_" pan="M14_TheaterIndex_HeadImg2">
                    <h2>《狂暴巨兽》</h2>
                    <a href="http://movie.mtime.com/225925/" title="《狂暴巨兽》" target="_blank"><img src="http://img5.mtime.cn/mg/2018/04/10/155555.67228607.jpg" width="1000" height="390" alt="《狂暴巨兽》" /></a>
                </dd>
            </dl>
        </div>
    </div>
</div>
<div class="filmcon">    <div class="isthefilm">                <div id="ticketSearchFixDiv" class="onlineticket">   		    <div class="midbox">                        	    <div class="cityselect">                    <h2>厦门</h2>                    <div id="changeCityDiv">                        <a href="#" class="citylink __r_c_" pan="M14_TheaterIndex_Search_City" onclick="return false;">切换城市</a>                    </div>                </div>                                <div id="ticketSearchDiv" class="movieselectbox clearfix">                </div>            </div>         </div>                <div id="M14_B_TheaterChannelIndex_AboveHotplayTG"></div>                 
<script type="text/javascript">
        var hotplaySvList = [{"Id":253823,"Url":"http://movie.mtime.com/253823/","Title":"后来的我们"},{"Id":233465,"Url":"http://movie.mtime.com/233465/","Title":"幕后玩家"},{"Id":225925,"Url":"http://movie.mtime.com/225925/","Title":"狂暴巨兽"},{"Id":240937,"Url":"http://movie.mtime.com/240937/","Title":"低压槽：欲望之城"},{"Id":211987,"Url":"http://movie.mtime.com/211987/","Title":"战神纪"},{"Id":219107,"Url":"http://movie.mtime.com/219107/","Title":"头号玩家"},{"Id":238459,"Url":"http://movie.mtime.com/238459/","Title":"玛丽与魔女之花"},{"Id":237363,"Url":"http://movie.mtime.com/237363/","Title":"犬之岛"},{"Id":236456,"Url":"http://movie.mtime.com/236456/","Title":"黄金花"},{"Id":254741,"Url":"http://movie.mtime.com/254741/","Title":"厉害了，我的国"},{"Id":253263,"Url":"http://movie.mtime.com/253263/","Title":"21克拉"},{"Id":228947,"Url":"http://movie.mtime.com/228947/","Title":"巴霍巴利王2：终结"},{"Id":256011,"Url":"http://movie.mtime.com/256011/","Title":"午夜十二点"},{"Id":236671,"Url":"http://movie.mtime.com/236671/","Title":"冰雪女王3：火与冰"},{"Id":244987,"Url":"http://movie.mtime.com/244987/","Title":"香港大营救"},{"Id":254850,"Url":"http://movie.mtime.com/254850/","Title":"出山记"},{"Id":247295,"Url":"http://movie.mtime.com/247295/","Title":"我是你妈"},{"Id":217497,"Url":"http://movie.mtime.com/217497/","Title":"复仇者联盟3：无限战争"},{"Id":229261,"Url":"http://movie.mtime.com/229261/","Title":"战犬瑞克斯"}];
</script>


    <div class="isthebox">
        <div class="title clearfix">
            <h2 class="fl">正在热映<span>19</span>部</h2>
            <div id="hotplayMenu" class="filmlink fl __r_c_" pan="M14_TheaterIndex_HotplayMenu">
                <a href="#" class="on" onclick="return false;">全部<span>|</span></a>
                <a href="#" onclick="return false;">3D<span>|</span></a>
                <a href="#" onclick="return false;">IMAX<span>|</span></a>
                <a href="#" onclick="return false;">冒险<span>|</span></a>           
                <a href="#" onclick="return false;">动作<span>|</span></a>           
                <a href="#" onclick="return false;">科幻<span>|</span></a>           
                <a href="#" onclick="return false;">奇幻<span>|</span></a>           
                <a href="#" onclick="return false;">喜剧</a>
            </div>
            
            <div class="citysearch __r_c_" pan="M14_TheaterIndex_HotplaySearch">
                <input id="hotplaySearchText" type="text" class="text" value="搜索影片" />
                <input id="hotplaySearchButton" type="button" class="button" />
            </div>
            <dl id="hotplaySearchResultDl" class="showsearch searchcity __r_c_" style="display:none;top:42px;" pan="M14_TheaterIndex_HotplaySearch">
            </dl>
        </div>
        <div id="hotplayContent">
         
        <div>
            <div class="moviebox clearfix">
            
      	        <div class="firstmovie fl">
        	        <dl>
            	        <dt>
                            <a href="http://movie.mtime.com/253823/" title="后来的我们/Us And Them(2018)" class="__r_c_" pan="M14_TheaterIndex_Hotplay_FirstCover" target="_blank"><img width="270" height="360" src="http://img5.mtime.cn/mt/2018/04/23/152454.82425063_270X360X4.jpg" alt="后来的我们/Us And Them(2018)"></a><span class="banben"></span>
                        </dt>
                        <dd>                        
                            
                	        <div class="score none" mid="253823"></div>
                	        <h2><a href="http://movie.mtime.com/253823/" target="_blank" class="__r_c_" pan="M14_TheaterIndex_Hotplay_FirstTitle">后来的我们</a></h2>
                            <h3 class="__r_c_" pan="M14_TheaterIndex_Hotplay_FirstTitle">120分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Romance" target="_blank">爱情</a></h3>
                            <p class="hotmovie"><i class="ico_dot"></i>井柏然周冬雨演绎十年甜虐故事</p>
                            <div class="moviebtn">
                                <strong>33</strong>元起
                                <a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/253823/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_FirstButton" target="_blank">选座购票</a>
                            </div>
                        </dd>
                    </dl>
                </div>
            
                <div class="othermovie fr">
                    <ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/233465/" title="幕后玩家/A or B(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/23/105105.36604810_100X140X4.jpg" alt="幕后玩家/A or B(2018)"><span class="score none" mid="233465"></span><i class="icon_hot"></i><span class="banben"><i class="icon_imax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/233465/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">幕后玩家</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">114分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
                <dd>33家影院上映257场</dd>
            <dd class="hot"><i class="ico_dot"></i>徐峥被困密室面临生死抉择</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/233465/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/225925/" title="狂暴巨兽/Rampage(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/12/094135.36237108_100X140X4.jpg" alt="狂暴巨兽/Rampage(2018)"><span class="score none" mid="225925"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/225925/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">狂暴巨兽</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">108分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>31家影院上映173场</dd>
            <dd class="hot"><i class="ico_dot"></i>强森带领"拯救世界小队"逆袭巨兽</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/225925/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/240937/" title="低压槽：欲望之城/The Trough(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/09/145333.69838114_100X140X4.jpg" alt="低压槽：欲望之城/The Trough(2018)"><span class="score none" mid="240937"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/240937/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">低压槽：欲望之城</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">112分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Crime" target="_blank">犯罪</a></dd>
                <dd>20家影院上映62场</dd>
            <dd class="hot"><i class="ico_dot"></i>张家辉自导自演孤胆卧底英雄</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/240937/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/211987/" title="战神纪/Genghis Khan(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/24/232225.29539916_100X140X4.jpg" alt="战神纪/Genghis Khan(2018)"><span class="score none" mid="211987"></span><span class="banben"><i class="icon_3d"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/211987/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">战神纪</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">119分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
                <dd>22家影院上映57场</dd>
            <dd class="hot"><i class="ico_dot"></i>陈伟霆林允演绎铁木真传奇故事</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/211987/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/219107/" title="头号玩家/Ready Player One(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/23/094042.12197321_100X140X4.jpg" alt="头号玩家/Ready Player One(2018)"><span class="score none" mid="219107"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/219107/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">头号玩家</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">140分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>14家影院上映56场</dd>
            <dd class="hot"><i class="ico_dot"></i>斯皮尔伯格玩转VR虚拟世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/219107/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/238459/" title="玛丽与魔女之花/Mary and the Witch's Flower(2017)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/18/154120.76776385_100X140X4.jpg" alt="玛丽与魔女之花/Mary and the Witch's Flower(2017)"><span class="score none" mid="238459"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/238459/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">玛丽与魔女之花</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">103分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>17家影院上映26场</dd>
            <dd class="hot"><i class="ico_dot"></i>21世纪的"魔女宅急便"</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/238459/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul>
                </div>
            </div>
            <div id="hotplayMoreDiv" class="moviemore none">
      	            <div class="othermovie">
                        
<ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/237363/" title="犬之岛/Isle of Dogs(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/10/105003.83390930_100X140X4.jpg" alt="犬之岛/Isle of Dogs(2018)"><span class="score none" mid="237363"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/237363/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">犬之岛</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">101分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>5家影院上映12场</dd>
            <dd class="hot"><i class="ico_dot"></i>韦斯安德森创造奇妙狗狗世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/237363/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/236456/" title="黄金花/Tomorrow Is Another Day(2017)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/23/181343.22054563_100X140X4.jpg" alt="黄金花/Tomorrow Is Another Day(2017)"><span class="score none" mid="236456"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/236456/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">黄金花</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">91分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
                <dd>5家影院上映9场</dd>
            <dd class="hot"><i class="ico_dot"></i>毛舜筠演绎坚强妈妈勇夺金像影后</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/236456/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/254741/" title="厉害了，我的国/Amazing China(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/02/22/142010.67656990_100X140X4.jpg" alt="厉害了，我的国/Amazing China(2018)"><span class="score none" mid="254741"></span><span class="banben"><i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/254741/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">厉害了，我的国</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">90分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Documentary" target="_blank">纪录片</a></dd>
                <dd>4家影院上映7场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/254741/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/253263/" title="21克拉/21 Karat(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/19/171513.55903809_100X140X4.jpg" alt="21克拉/21 Karat(2018)"><span class="score none" mid="253263"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/253263/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">21克拉</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">96分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Romance" target="_blank">爱情</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
                <dd>2家影院上映6场</dd>
            <dd class="hot"><i class="ico_dot"></i>奢侈女迪丽热巴遇上勤俭男郭京飞</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/253263/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/228947/" title="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/26/095604.57058697_100X140X4.jpg" alt="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)"><span class="score none" mid="228947"></span><span class="banben"><i class="icon_imax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/228947/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">巴霍巴利王2：终结</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">141分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a></dd>
                <dd>3家影院上映3场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/228947/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/256011/" title="午夜十二点/Midnight Ⅻ(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/04/142026.15617294_100X140X4.jpg" alt="午夜十二点/Midnight Ⅻ(2018)"><span class="score none" mid="256011"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/256011/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">午夜十二点</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">87分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Thriller" target="_blank">惊悚</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Horror" target="_blank">恐怖</a></dd>
                <dd>2家影院上映2场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/256011/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/236671/" title="冰雪女王3：火与冰/The Snow Queen 3: Fire and Ice(2016)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/11/170904.92580566_100X140X4.jpg" alt="冰雪女王3：火与冰/The Snow Queen 3: Fire and Ice(2016)"><span class="score none" mid="236671"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/236671/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">冰雪女王3：火与冰</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">90分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>1家影院上映1场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/236671/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/244987/" title="香港大营救/Hong Kong Rescue(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/23/155159.74258787_100X140X4.jpg" alt="香港大营救/Hong Kong Rescue(2018)"><span class="score none" mid="244987"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/244987/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">香港大营救</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">95分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Mystery" target="_blank">悬疑</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/244987/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/254850/" title="出山记/Beyond the mountains(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/07/093413.25173344_100X140X4.jpg" alt="出山记/Beyond the mountains(2018)"><span class="score none" mid="254850"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/254850/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">出山记</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">98分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Documentary" target="_blank">纪录片</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/254850/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/247295/" title="我是你妈/I Am Your Mom(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2017/12/28/111142.40724364_100X140X4.jpg" alt="我是你妈/I Am Your Mom(2018)"><span class="score none" mid="247295"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/247295/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">我是你妈</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">104分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/247295/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/217497/" title="复仇者联盟3：无限战争/Avengers: Infinity War(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/30/101316.99752366_100X140X4.jpg" alt="复仇者联盟3：无限战争/Avengers: Infinity War(2018)"><span class="score none" mid="217497"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/217497/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">复仇者联盟3：无限战争</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">150分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/217497/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/229261/" title="战犬瑞克斯/Megan Leavey(2017)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/24/152254.36892172_100X140X4.jpg" alt="战犬瑞克斯/Megan Leavey(2017)"><span class="score none" mid="229261"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/229261/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">战犬瑞克斯</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">116分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Biography" target="_blank">传记</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/229261/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul>                    </div>
            </div>
            
            <div class="i_more"><a href="#" id="hotplayMoreLink" class="__r_c_" pan="M14_TheaterIndex_Hotplay_More" onclick="return false;"><i></i>更多</a></div>
        </div>
         
        <div class="none">
            <div class="moviemore">
      	        <div class="othermovie">
                    <ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/233465/" title="幕后玩家/A or B(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/23/105105.36604810_100X140X4.jpg" alt="幕后玩家/A or B(2018)"><span class="score none" mid="233465"></span><i class="icon_hot"></i><span class="banben"><i class="icon_imax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/233465/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">幕后玩家</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">114分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
                <dd>33家影院上映257场</dd>
            <dd class="hot"><i class="ico_dot"></i>徐峥被困密室面临生死抉择</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/233465/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/225925/" title="狂暴巨兽/Rampage(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/12/094135.36237108_100X140X4.jpg" alt="狂暴巨兽/Rampage(2018)"><span class="score none" mid="225925"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/225925/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">狂暴巨兽</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">108分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>31家影院上映173场</dd>
            <dd class="hot"><i class="ico_dot"></i>强森带领"拯救世界小队"逆袭巨兽</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/225925/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/211987/" title="战神纪/Genghis Khan(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/24/232225.29539916_100X140X4.jpg" alt="战神纪/Genghis Khan(2018)"><span class="score none" mid="211987"></span><span class="banben"><i class="icon_3d"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/211987/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">战神纪</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">119分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
                <dd>22家影院上映57场</dd>
            <dd class="hot"><i class="ico_dot"></i>陈伟霆林允演绎铁木真传奇故事</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/211987/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/219107/" title="头号玩家/Ready Player One(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/23/094042.12197321_100X140X4.jpg" alt="头号玩家/Ready Player One(2018)"><span class="score none" mid="219107"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/219107/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">头号玩家</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">140分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>14家影院上映56场</dd>
            <dd class="hot"><i class="ico_dot"></i>斯皮尔伯格玩转VR虚拟世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/219107/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/254741/" title="厉害了，我的国/Amazing China(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/02/22/142010.67656990_100X140X4.jpg" alt="厉害了，我的国/Amazing China(2018)"><span class="score none" mid="254741"></span><span class="banben"><i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/254741/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">厉害了，我的国</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">90分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Documentary" target="_blank">纪录片</a></dd>
                <dd>4家影院上映7场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/254741/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/228947/" title="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/26/095604.57058697_100X140X4.jpg" alt="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)"><span class="score none" mid="228947"></span><span class="banben"><i class="icon_imax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/228947/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">巴霍巴利王2：终结</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">141分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a></dd>
                <dd>3家影院上映3场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/228947/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/217497/" title="复仇者联盟3：无限战争/Avengers: Infinity War(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/30/101316.99752366_100X140X4.jpg" alt="复仇者联盟3：无限战争/Avengers: Infinity War(2018)"><span class="score none" mid="217497"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/217497/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">复仇者联盟3：无限战争</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">150分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/217497/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul>
                </div>
            </div>
        </div>
         
        <div class="none">
            <div class="moviemore">
      	        <div class="othermovie">
                    <ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/233465/" title="幕后玩家/A or B(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/23/105105.36604810_100X140X4.jpg" alt="幕后玩家/A or B(2018)"><span class="score none" mid="233465"></span><i class="icon_hot"></i><span class="banben"><i class="icon_imax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/233465/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">幕后玩家</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">114分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
                <dd>33家影院上映257场</dd>
            <dd class="hot"><i class="ico_dot"></i>徐峥被困密室面临生死抉择</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/233465/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/225925/" title="狂暴巨兽/Rampage(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/12/094135.36237108_100X140X4.jpg" alt="狂暴巨兽/Rampage(2018)"><span class="score none" mid="225925"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/225925/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">狂暴巨兽</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">108分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>31家影院上映173场</dd>
            <dd class="hot"><i class="ico_dot"></i>强森带领"拯救世界小队"逆袭巨兽</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/225925/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/219107/" title="头号玩家/Ready Player One(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/23/094042.12197321_100X140X4.jpg" alt="头号玩家/Ready Player One(2018)"><span class="score none" mid="219107"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/219107/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">头号玩家</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">140分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>14家影院上映56场</dd>
            <dd class="hot"><i class="ico_dot"></i>斯皮尔伯格玩转VR虚拟世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/219107/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/254741/" title="厉害了，我的国/Amazing China(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/02/22/142010.67656990_100X140X4.jpg" alt="厉害了，我的国/Amazing China(2018)"><span class="score none" mid="254741"></span><span class="banben"><i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/254741/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">厉害了，我的国</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">90分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Documentary" target="_blank">纪录片</a></dd>
                <dd>4家影院上映7场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/254741/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/228947/" title="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/26/095604.57058697_100X140X4.jpg" alt="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)"><span class="score none" mid="228947"></span><span class="banben"><i class="icon_imax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/228947/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">巴霍巴利王2：终结</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">141分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a></dd>
                <dd>3家影院上映3场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/228947/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/217497/" title="复仇者联盟3：无限战争/Avengers: Infinity War(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/30/101316.99752366_100X140X4.jpg" alt="复仇者联盟3：无限战争/Avengers: Infinity War(2018)"><span class="score none" mid="217497"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/217497/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">复仇者联盟3：无限战争</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">150分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/217497/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul>
                </div>
            </div>
        </div>
         
        <div class="none">
            <div class="moviemore">
      	        <div class="othermovie">
                    <ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/225925/" title="狂暴巨兽/Rampage(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/12/094135.36237108_100X140X4.jpg" alt="狂暴巨兽/Rampage(2018)"><span class="score none" mid="225925"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/225925/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">狂暴巨兽</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">108分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>31家影院上映173场</dd>
            <dd class="hot"><i class="ico_dot"></i>强森带领"拯救世界小队"逆袭巨兽</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/225925/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/211987/" title="战神纪/Genghis Khan(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/24/232225.29539916_100X140X4.jpg" alt="战神纪/Genghis Khan(2018)"><span class="score none" mid="211987"></span><span class="banben"><i class="icon_3d"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/211987/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">战神纪</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">119分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
                <dd>22家影院上映57场</dd>
            <dd class="hot"><i class="ico_dot"></i>陈伟霆林允演绎铁木真传奇故事</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/211987/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/219107/" title="头号玩家/Ready Player One(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/23/094042.12197321_100X140X4.jpg" alt="头号玩家/Ready Player One(2018)"><span class="score none" mid="219107"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/219107/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">头号玩家</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">140分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>14家影院上映56场</dd>
            <dd class="hot"><i class="ico_dot"></i>斯皮尔伯格玩转VR虚拟世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/219107/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/238459/" title="玛丽与魔女之花/Mary and the Witch's Flower(2017)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/18/154120.76776385_100X140X4.jpg" alt="玛丽与魔女之花/Mary and the Witch's Flower(2017)"><span class="score none" mid="238459"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/238459/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">玛丽与魔女之花</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">103分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>17家影院上映26场</dd>
            <dd class="hot"><i class="ico_dot"></i>21世纪的"魔女宅急便"</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/238459/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/237363/" title="犬之岛/Isle of Dogs(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/10/105003.83390930_100X140X4.jpg" alt="犬之岛/Isle of Dogs(2018)"><span class="score none" mid="237363"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/237363/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">犬之岛</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">101分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>5家影院上映12场</dd>
            <dd class="hot"><i class="ico_dot"></i>韦斯安德森创造奇妙狗狗世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/237363/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/236671/" title="冰雪女王3：火与冰/The Snow Queen 3: Fire and Ice(2016)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/11/170904.92580566_100X140X4.jpg" alt="冰雪女王3：火与冰/The Snow Queen 3: Fire and Ice(2016)"><span class="score none" mid="236671"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/236671/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">冰雪女王3：火与冰</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">90分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>1家影院上映1场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/236671/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/244987/" title="香港大营救/Hong Kong Rescue(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/23/155159.74258787_100X140X4.jpg" alt="香港大营救/Hong Kong Rescue(2018)"><span class="score none" mid="244987"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/244987/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">香港大营救</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">95分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Mystery" target="_blank">悬疑</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/244987/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/217497/" title="复仇者联盟3：无限战争/Avengers: Infinity War(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/30/101316.99752366_100X140X4.jpg" alt="复仇者联盟3：无限战争/Avengers: Infinity War(2018)"><span class="score none" mid="217497"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/217497/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">复仇者联盟3：无限战争</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">150分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/217497/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul>
                </div>
            </div>
        </div>
        <div class="none">
            <div class="moviemore">
      	        <div class="othermovie">
                    <ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/225925/" title="狂暴巨兽/Rampage(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/12/094135.36237108_100X140X4.jpg" alt="狂暴巨兽/Rampage(2018)"><span class="score none" mid="225925"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/225925/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">狂暴巨兽</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">108分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>31家影院上映173场</dd>
            <dd class="hot"><i class="ico_dot"></i>强森带领"拯救世界小队"逆袭巨兽</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/225925/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/219107/" title="头号玩家/Ready Player One(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/23/094042.12197321_100X140X4.jpg" alt="头号玩家/Ready Player One(2018)"><span class="score none" mid="219107"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/219107/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">头号玩家</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">140分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>14家影院上映56场</dd>
            <dd class="hot"><i class="ico_dot"></i>斯皮尔伯格玩转VR虚拟世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/219107/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/228947/" title="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/26/095604.57058697_100X140X4.jpg" alt="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)"><span class="score none" mid="228947"></span><span class="banben"><i class="icon_imax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/228947/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">巴霍巴利王2：终结</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">141分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a></dd>
                <dd>3家影院上映3场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/228947/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/244987/" title="香港大营救/Hong Kong Rescue(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/23/155159.74258787_100X140X4.jpg" alt="香港大营救/Hong Kong Rescue(2018)"><span class="score none" mid="244987"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/244987/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">香港大营救</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">95分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Mystery" target="_blank">悬疑</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/244987/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/217497/" title="复仇者联盟3：无限战争/Avengers: Infinity War(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/30/101316.99752366_100X140X4.jpg" alt="复仇者联盟3：无限战争/Avengers: Infinity War(2018)"><span class="score none" mid="217497"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/217497/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">复仇者联盟3：无限战争</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">150分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/217497/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul>
                </div>
            </div>
        </div>
        <div class="none">
            <div class="moviemore">
      	        <div class="othermovie">
                    <ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/225925/" title="狂暴巨兽/Rampage(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/12/094135.36237108_100X140X4.jpg" alt="狂暴巨兽/Rampage(2018)"><span class="score none" mid="225925"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/225925/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">狂暴巨兽</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">108分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>31家影院上映173场</dd>
            <dd class="hot"><i class="ico_dot"></i>强森带领"拯救世界小队"逆袭巨兽</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/225925/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/219107/" title="头号玩家/Ready Player One(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/23/094042.12197321_100X140X4.jpg" alt="头号玩家/Ready Player One(2018)"><span class="score none" mid="219107"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/219107/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">头号玩家</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">140分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>14家影院上映56场</dd>
            <dd class="hot"><i class="ico_dot"></i>斯皮尔伯格玩转VR虚拟世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/219107/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/237363/" title="犬之岛/Isle of Dogs(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/10/105003.83390930_100X140X4.jpg" alt="犬之岛/Isle of Dogs(2018)"><span class="score none" mid="237363"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/237363/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">犬之岛</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">101分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>5家影院上映12场</dd>
            <dd class="hot"><i class="ico_dot"></i>韦斯安德森创造奇妙狗狗世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/237363/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/236671/" title="冰雪女王3：火与冰/The Snow Queen 3: Fire and Ice(2016)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/11/170904.92580566_100X140X4.jpg" alt="冰雪女王3：火与冰/The Snow Queen 3: Fire and Ice(2016)"><span class="score none" mid="236671"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/236671/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">冰雪女王3：火与冰</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">90分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>1家影院上映1场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/236671/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/217497/" title="复仇者联盟3：无限战争/Avengers: Infinity War(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/30/101316.99752366_100X140X4.jpg" alt="复仇者联盟3：无限战争/Avengers: Infinity War(2018)"><span class="score none" mid="217497"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/217497/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">复仇者联盟3：无限战争</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">150分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/217497/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul>
                </div>
            </div>
        </div>
        <div class="none">
            <div class="moviemore">
      	        <div class="othermovie">
                    <ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/211987/" title="战神纪/Genghis Khan(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/24/232225.29539916_100X140X4.jpg" alt="战神纪/Genghis Khan(2018)"><span class="score none" mid="211987"></span><span class="banben"><i class="icon_3d"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/211987/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">战神纪</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">119分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></dd>
                <dd>22家影院上映57场</dd>
            <dd class="hot"><i class="ico_dot"></i>陈伟霆林允演绎铁木真传奇故事</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/211987/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/237363/" title="犬之岛/Isle of Dogs(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/10/105003.83390930_100X140X4.jpg" alt="犬之岛/Isle of Dogs(2018)"><span class="score none" mid="237363"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/237363/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">犬之岛</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">101分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>5家影院上映12场</dd>
            <dd class="hot"><i class="ico_dot"></i>韦斯安德森创造奇妙狗狗世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/237363/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/228947/" title="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/26/095604.57058697_100X140X4.jpg" alt="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)"><span class="score none" mid="228947"></span><span class="banben"><i class="icon_imax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/228947/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">巴霍巴利王2：终结</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">141分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a></dd>
                <dd>3家影院上映3场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/228947/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul><ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/217497/" title="复仇者联盟3：无限战争/Avengers: Infinity War(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/30/101316.99752366_100X140X4.jpg" alt="复仇者联盟3：无限战争/Avengers: Infinity War(2018)"><span class="score none" mid="217497"></span><span class="banben"><i class="icon_3d"></i>
<i class="icon_3dimax"></i>
<i class="icon_dmax"></i>
</span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/217497/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">复仇者联盟3：无限战争</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">150分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/217497/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul>
                </div>
            </div>
        </div>
        <div class="none">
            <div class="moviemore">
      	        <div class="othermovie">
                    <ul class="clearfix">    <li class="clearfix">
        <a href="http://movie.mtime.com/237363/" title="犬之岛/Isle of Dogs(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/04/10/105003.83390930_100X140X4.jpg" alt="犬之岛/Isle of Dogs(2018)"><span class="score none" mid="237363"></span><span class="banben"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/237363/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">犬之岛</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">101分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>5家影院上映12场</dd>
            <dd class="hot"><i class="ico_dot"></i>韦斯安德森创造奇妙狗狗世界</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/237363/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/236671/" title="冰雪女王3：火与冰/The Snow Queen 3: Fire and Ice(2016)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2018/03/11/170904.92580566_100X140X4.jpg" alt="冰雪女王3：火与冰/The Snow Queen 3: Fire and Ice(2016)"><span class="score none" mid="236671"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/236671/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">冰雪女王3：火与冰</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">90分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></dd>
                <dd>1家影院上映1场</dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/236671/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
    <li class="clearfix">
        <a href="http://movie.mtime.com/247295/" title="我是你妈/I Am Your Mom(2018)" target="_blank" class="picbox __r_c_" pan="M14_TheaterIndex_Hotplay_Cover"><img src="http://img5.mtime.cn/mt/2017/12/28/111142.40724364_100X140X4.jpg" alt="我是你妈/I Am Your Mom(2018)"><span class="score none" mid="247295"></span></a>
        <dl>
            <dt><a href="http://movie.mtime.com/247295/" class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text" target="_blank">我是你妈</a></dt>
            <dd class="__r_c_" pan="M14_TheaterIndex_Hotplay_Text">104分钟 - <a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a></dd>
            <dd class="btns"><a href="http://theater.mtime.com/China_Fujian_Province_Xiamen/movie/247295/" class="ticket __r_c_" pan="M14_TheaterIndex_Hotplay_Button" target="_blank">选座购票</a></dd>
        </dl>
    </li>
</ul>
                </div>
            </div>
        </div>
        </div>
     </div>    </div>        <div id="M14_B_TheaterChannelIndex_AboveUpcomingTG"></div>         
<div class="upcoming" id="backHere">
    <div class="title">
        <h2>即将上映 －5月4日~8月1日 </h2>
    </div> 
    <div id="upcomingRegion" class="i_swwantlist" mids="244987,228947,256264,229345,256122,217497,256235,227955,229261,256115,247295,256291,237551,250858,250729,256312,256116,256234,240384,256236,225774,232316,250633,256298,255266,254656,252897,251071,256346,256311,256276,234987,256141,256252,225759,254772,236846,255800,242396,240989,242167,256244,256241,229366,253781,232758,253688"> 
        <a href="#" id="upcomingPre" title="last" class="lastcol" style="display:none;"></a>
        <a href="#" id="upcomingNext" title="next" class="nextcol" style="display:none;"></a>
        <span class="shadow"></span>
        <div class="i_swwantlister ">
            <dl id="upcomingSlide" class="clearfix transition6" style="width:15040px;">
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月4日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/244987/" target="_blank" title="香港大营救/Hong Kong Rescue(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/23/155159.74258787_100X150X4.jpg" width="100" height="150" alt="香港大营救/Hong Kong Rescue(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/244987/" target="_blank">香港大营救</a></h3>
                                <p><span mid="244987" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Mystery" target="_blank">悬疑</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1505950/" target="_blank">刘一君</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/244987/trailer/70414.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="244987" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月4日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/228947/" target="_blank" title="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/26/095604.57058697_100X150X4.jpg" width="100" height="150" alt="巴霍巴利王2：终结/Baahubali 2: The Conclusion(2017)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/228947/" target="_blank">巴霍巴利王2：终结</a></h3>
                                <p><span mid="228947" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1593078/" target="_blank">S·S·拉贾穆里</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/228947/trailer/70419.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="228947" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月5日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256264/" target="_blank" title="灵妖鉴之盘丝小仙(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/28/164857.45381038_100X150X4.jpg" width="100" height="150" alt="灵妖鉴之盘丝小仙(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256264/" target="_blank">灵妖鉴之盘丝小仙</a></h3>
                                <p><span mid="256264" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2330807/" target="_blank">刘弘扬</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256264" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月5日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/229345/" target="_blank" title="青年马克思/Le jeune Karl Marx(2017)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/05/02/144324.94176866_100X150X4.jpg" width="100" height="150" alt="青年马克思/Le jeune Karl Marx(2017)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/229345/" target="_blank">青年马克思</a></h3>
                                <p><span mid="229345" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Biography" target="_blank">传记</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1148508/" target="_blank">拉乌尔·佩克</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/229345/trailer/70420.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="229345" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月7日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256122/" target="_blank" title="任性的硬币/The Coin(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/18/104709.53283255_100X150X4.jpg" width="100" height="150" alt="任性的硬币/The Coin(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256122/" target="_blank">任性的硬币</a></h3>
                                <p><span mid="256122" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1967015/" target="_blank">陈之月</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256122" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月11日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/217497/" target="_blank" title="复仇者联盟3：无限战争/Avengers: Infinity War(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/03/30/101316.99752366_100X150X4.jpg" width="100" height="150" alt="复仇者联盟3：无限战争/Avengers: Infinity War(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/217497/" target="_blank">复仇者联盟3：无..</a></h3>
                                <p><span mid="217497" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/903229/" target="_blank">安东尼·罗素</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/217497/trailer/70349.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="217497" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月11日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256235/" target="_blank" title="破门/You'll Never Walk Alone(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/17/093909.52731304_100X150X4.jpg" width="100" height="150" alt="破门/You'll Never Walk Alone(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256235/" target="_blank">破门</a></h3>
                                <p><span mid="256235" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/892973/" target="_blank">徐耿</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/256235/trailer/70425.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256235" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月11日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/227955/" target="_blank" title="寻找女神&#183;娇阿依(2016)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2016/09/28/103922.30788799_100X150X4.jpg" width="100" height="150" alt="寻找女神&#183;娇阿依(2016)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/227955/" target="_blank">寻找女神·娇阿依</a></h3>
                                <p><span mid="227955" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2235514/" target="_blank">赵章翔</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="227955" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月11日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/229261/" target="_blank" title="战犬瑞克斯/Megan Leavey(2017)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/24/152254.36892172_100X150X4.jpg" width="100" height="150" alt="战犬瑞克斯/Megan Leavey(2017)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/229261/" target="_blank">战犬瑞克斯</a></h3>
                                <p><span mid="229261" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Biography" target="_blank">传记</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1879111/" target="_blank">加比里埃拉·考珀斯维特</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/229261/trailer/70185.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="229261" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月11日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256115/" target="_blank" title="天梦/The Dream(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/08/183655.37701943_100X150X4.jpg" width="100" height="150" alt="天梦/The Dream(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256115/" target="_blank">天梦</a></h3>
                                <p><span mid="256115" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2329789/" target="_blank">许文琦</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256115" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月11日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/247295/" target="_blank" title="我是你妈/I Am Your Mom(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2017/12/28/111142.40724364_100X150X4.jpg" width="100" height="150" alt="我是你妈/I Am Your Mom(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/247295/" target="_blank">我是你妈</a></h3>
                                <p><span mid="247295" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1318607/" target="_blank">张骁</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/247295/trailer/70322.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="247295" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月13日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256291/" target="_blank" title="天下父母(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/26/152357.36682756_100X150X4.jpg" width="100" height="150" alt="天下父母(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256291/" target="_blank">天下父母</a></h3>
                                <p><span mid="256291" method="want" genre="0"></span></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1743569/" target="_blank">崔守杰</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256291" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月17日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/237551/" target="_blank" title="路过未来/Walking Past the Future(2017)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/12/094019.48070147_100X150X4.jpg" width="100" height="150" alt="路过未来/Walking Past the Future(2017)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/237551/" target="_blank">路过未来</a></h3>
                                <p><span mid="237551" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1552980/" target="_blank">李睿珺</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/237551/trailer/70338.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="237551" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月18日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/250858/" target="_blank" title="寂静之地/A Quiet Place(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/10/094358.70001177_100X150X4.jpg" width="100" height="150" alt="寂静之地/A Quiet Place(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/250858/" target="_blank">寂静之地</a></h3>
                                <p><span mid="250858" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Horror" target="_blank">恐怖</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/928550/" target="_blank">约翰·卡拉辛斯基</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/250858/trailer/70415.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="250858" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月18日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/250729/" target="_blank" title="超时空同居/How Long Will I Love U(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/20/170922.23736012_100X150X4.jpg" width="100" height="150" alt="超时空同居/How Long Will I Love U(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/250729/" target="_blank">超时空同居</a></h3>
                                <p><span mid="250729" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2054611/" target="_blank">苏伦</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/250729/trailer/70123.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="250729" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月18日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256312/" target="_blank" title="火魔高跟鞋/The High Heels(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/28/145347.11296236_100X150X4.jpg" width="100" height="150" alt="火魔高跟鞋/The High Heels(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256312/" target="_blank">火魔高跟鞋</a></h3>
                                <p><span mid="256312" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2331080/" target="_blank">耿兴隆</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256312" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月18日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256116/" target="_blank" title="荒城纪/The Lost Land(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/17/143947.17272696_100X150X4.jpg" width="100" height="150" alt="荒城纪/The Lost Land(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256116/" target="_blank">荒城纪</a></h3>
                                <p><span mid="256116" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1022437/" target="_blank">徐啸力</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256116" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月18日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256234/" target="_blank" title="擒贼先擒王(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/25/114441.21660137_100X150X4.jpg" width="100" height="150" alt="擒贼先擒王(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256234/" target="_blank">擒贼先擒王</a></h3>
                                <p><span mid="256234" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2330795/" target="_blank">李相国</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/256234/trailer/70423.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256234" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月18日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/240384/" target="_blank" title="昼颜/Hirugao: Love Affairs in the Afternoon(2017)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/23/114212.83150282_100X150X4.jpg" width="100" height="150" alt="昼颜/Hirugao: Love Affairs in the Afternoon(2017)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/240384/" target="_blank">昼颜</a></h3>
                                <p><span mid="240384" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Romance" target="_blank">爱情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1098407/" target="_blank">西谷弘</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/240384/trailer/70305.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="240384" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月25日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256236/" target="_blank" title="时间暗局/Conspiracy(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/24/180507.50944500_100X150X4.jpg" width="100" height="150" alt="时间暗局/Conspiracy(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256236/" target="_blank">时间暗局</a></h3>
                                <p><span mid="256236" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Mystery" target="_blank">悬疑</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2330793/" target="_blank">陈亮言</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256236" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月25日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/225774/" target="_blank" title="命运速递/FATE EXPRESS(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/26/141528.31274809_100X150X4.jpg" width="100" height="150" alt="命运速递/FATE EXPRESS(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/225774/" target="_blank">命运速递</a></h3>
                                <p><span mid="225774" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1962325/" target="_blank">李非</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/225774/trailer/70345.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="225774" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月25日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/232316/" target="_blank" title="完美陌生人/Perfetti sconosciuti(2016)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/27/093654.46836587_100X150X4.jpg" width="100" height="150" alt="完美陌生人/Perfetti sconosciuti(2016)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/232316/" target="_blank">完美陌生人</a></h3>
                                <p><span mid="232316" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1477702/" target="_blank">保罗·格诺维瑟</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/232316/trailer/70407.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="232316" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月25日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/250633/" target="_blank" title="西小河的夏天/End Of Summer(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/05/02/103859.22726064_100X150X4.jpg" width="100" height="150" alt="西小河的夏天/End Of Summer(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/250633/" target="_blank">西小河的夏天</a></h3>
                                <p><span mid="250633" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2106603/" target="_blank">周全</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/250633/trailer/68108.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="250633" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月29日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256298/" target="_blank" title="爱是永恒/Eternal Love(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/27/140820.75209718_100X150X4.jpg" width="100" height="150" alt="爱是永恒/Eternal Love(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256298/" target="_blank">爱是永恒</a></h3>
                                <p><span mid="256298" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Romance" target="_blank">爱情</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2232843/" target="_blank">陈烈</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256298" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>5月31日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/255266/" target="_blank" title="魔镜奇缘2/Magic Mirror 2(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/03/12/094124.57605501_100X150X4.jpg" width="100" height="150" alt="魔镜奇缘2/Magic Mirror 2(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/255266/" target="_blank">魔镜奇缘2</a></h3>
                                <p><span mid="255266" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Family" target="_blank">家庭</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1252878/" target="_blank">陈设</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/255266/trailer/70404.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="255266" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月1日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/254656/" target="_blank" title="潜艇总动员：海底两万里/Happy Little Submarine 20000 Leagues under the Sea(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/27/095229.49762915_100X150X4.jpg" width="100" height="150" alt="潜艇总动员：海底两万里/Happy Little Submarine 20000 Leagues under the Sea(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/254656/" target="_blank">潜艇总动员：海底..</a></h3>
                                <p><span mid="254656" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2027191/" target="_blank">申宇</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="254656" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月1日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/252897/" target="_blank" title="阳台上/On The Baicon(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/17/101714.15804269_100X150X4.jpg" width="100" height="150" alt="阳台上/On The Baicon(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/252897/" target="_blank">阳台上</a></h3>
                                <p><span mid="252897" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1299669/" target="_blank">张猛</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/252897/trailer/70326.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="252897" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月1日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/251071/" target="_blank" title="光影之战/Ghost Well(2017)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/17/154533.11589095_100X150X4.jpg" width="100" height="150" alt="光影之战/Ghost Well(2017)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/251071/" target="_blank">光影之战</a></h3>
                                <p><span mid="251071" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1259646/" target="_blank">陈耀华</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="251071" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月1日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256346/" target="_blank" title="毛骨悚然之红衣男孩/Damnation(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/05/02/102232.84541788_100X150X4.jpg" width="100" height="150" alt="毛骨悚然之红衣男孩/Damnation(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256346/" target="_blank">毛骨悚然之红衣男孩</a></h3>
                                <p><span mid="256346" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Thriller" target="_blank">惊悚</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Horror" target="_blank">恐怖</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2331477/" target="_blank">孙杰</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256346" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月8日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256311/" target="_blank" title="一个人的江湖/The Universe Of One's Own(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/28/120049.99357683_100X150X4.jpg" width="100" height="150" alt="一个人的江湖/The Universe Of One's Own(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256311/" target="_blank">一个人的江湖</a></h3>
                                <p><span mid="256311" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1175679/" target="_blank">喻亢</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256311" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月8日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256276/" target="_blank" title="因果启示录/Karma(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/28/141649.67406890_100X150X4.jpg" width="100" height="150" alt="因果启示录/Karma(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256276/" target="_blank">因果启示录</a></h3>
                                <p><span mid="256276" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2074294/" target="_blank">王陆涛</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/256276/trailer/70406.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256276" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月15日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/234987/" target="_blank" title="猛虫过江(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/03/20/093256.46423636_100X150X4.jpg" width="100" height="150" alt="猛虫过江(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/234987/" target="_blank">猛虫过江</a></h3>
                                <p><span mid="234987" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1598051/" target="_blank">小沈阳</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="234987" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月15日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256141/" target="_blank" title="家(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/26/153435.36315761_100X150X4.jpg" width="100" height="150" alt="家(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256141/" target="_blank">家</a></h3>
                                <p><span mid="256141" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Music" target="_blank">音乐</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1176850/" target="_blank">刘红梅</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256141" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月15日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256252/" target="_blank" title="时间监狱(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/20/143033.26942588_100X150X4.jpg" width="100" height="150" alt="时间监狱(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256252/" target="_blank">时间监狱</a></h3>
                                <p><span mid="256252" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Romance" target="_blank">爱情</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1286402/" target="_blank">丁文</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256252" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月15日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/225759/" target="_blank" title="侏罗纪世界2/Jurassic World: Fallen Kingdom(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/24/114747.31584443_100X150X4.jpg" width="100" height="150" alt="侏罗纪世界2/Jurassic World: Fallen Kingdom(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/225759/" target="_blank">侏罗纪世界2</a></h3>
                                <p><span mid="225759" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1310397/" target="_blank">胡安·安东尼奥·巴亚纳</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/225759/trailer/70402.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="225759" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月15日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/254772/" target="_blank" title="疯狂这一年/Feng Kuang Zhe Yi Nian(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/05/02/150206.35361247_100X150X4.jpg" width="100" height="150" alt="疯狂这一年/Feng Kuang Zhe Yi Nian(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/254772/" target="_blank">疯狂这一年</a></h3>
                                <p><span mid="254772" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2323095/" target="_blank">丁仕昀</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/254772/trailer/70421.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="254772" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月16日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/236846/" target="_blank" title="吃货宇宙/Foodiverse(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/03/29/113525.14933710_100X150X4.jpg" width="100" height="150" alt="吃货宇宙/Foodiverse(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/236846/" target="_blank">吃货宇宙</a></h3>
                                <p><span mid="236846" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2235303/" target="_blank">陈廖宇</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/236846/trailer/70072.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="236846" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月22日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/255800/" target="_blank" title="青春不留白/The Unrepentant Youth(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/27/100003.31136106_100X150X4.jpg" width="100" height="150" alt="青春不留白/The Unrepentant Youth(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/255800/" target="_blank">青春不留白</a></h3>
                                <p><span mid="255800" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Youth" target="_blank">青春</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1301215/" target="_blank">尹大为</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/255800/trailer/70323.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="255800" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月22日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/242396/" target="_blank" title="凤凰城遗忘录/Phoenix Forgotten(2017)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2017/04/13/145128.97252430_100X150X4.jpg" width="100" height="150" alt="凤凰城遗忘录/Phoenix Forgotten(2017)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/242396/" target="_blank">凤凰城遗忘录</a></h3>
                                <p><span mid="242396" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Sci-Fi" target="_blank">科幻</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Horror" target="_blank">恐怖</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1541190/" target="_blank">Justin Barber</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="242396" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>6月29日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/240989/" target="_blank" title="动物世界/Animal World(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/16/092757.87463145_100X150X4.jpg" width="100" height="150" alt="动物世界/Animal World(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/240989/" target="_blank">动物世界</a></h3>
                                <p><span mid="240989" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1251640/" target="_blank">韩延</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/240989/trailer/70162.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="240989" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>7月6日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/242167/" target="_blank" title="我不是药神/Dying To Survive(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/12/164549.86299238_100X150X4.jpg" width="100" height="150" alt="我不是药神/Dying To Survive(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/242167/" target="_blank">我不是药神</a></h3>
                                <p><span mid="242167" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2145801/" target="_blank">文牧野</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/242167/trailer/70214.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="242167" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>7月6日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256244/" target="_blank" title="新大头儿子和小头爸爸3：俄罗斯奇遇记(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/18/183453.40955725_100X150X4.jpg" width="100" height="150" alt="新大头儿子和小头爸爸3：俄罗斯奇遇记(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256244/" target="_blank">新大头儿子和小头..</a></h3>
                                <p><span mid="256244" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Animation" target="_blank">动画</a></p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256244" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>7月13日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/256241/" target="_blank" title="风语咒/The Wind Guardians(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/04/24/233823.42133089_100X150X4.jpg" width="100" height="150" alt="风语咒/The Wind Guardians(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/256241/" target="_blank">风语咒</a></h3>
                                <p><span mid="256241" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Adventure" target="_blank">冒险</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2330818/" target="_blank">刘阔</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/256241/trailer/70325.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="256241" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>7月13日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/229366/" target="_blank" title="查理九世/Charlie IX &amp; Dodomo(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/02/05/095859.14194300_100X150X4.jpg" width="100" height="150" alt="查理九世/Charlie IX &amp; Dodomo(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/229366/" target="_blank">查理九世</a></h3>
                                <p><span mid="229366" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Fantasy" target="_blank">奇幻</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1259510/" target="_blank">王竞</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/229366/trailer/69536.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="229366" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>7月20日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/253781/" target="_blank" title="初恋的滋味(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2017/12/21/163556.14633586_100X150X4.jpg" width="100" height="150" alt="初恋的滋味(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/253781/" target="_blank">初恋的滋味</a></h3>
                                <p><span mid="253781" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Romance" target="_blank">爱情</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Drama" target="_blank">剧情</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/1850913/" target="_blank">关尔</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="253781" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>7月27日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/232758/" target="_blank" title="狄仁杰之四大天王/Detective Dee The Four Heavenly Kings(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2018/03/19/115811.29791899_100X150X4.jpg" width="100" height="150" alt="狄仁杰之四大天王/Detective Dee The Four Heavenly Kings(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/232758/" target="_blank">狄仁杰之四大天王</a></h3>
                                <p><span mid="232758" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Action" target="_blank">动作</a> / <a href="http://movie.mtime.com/movie/search/section/?type=Mystery" target="_blank">悬疑</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/892903/" target="_blank">徐克</a> </p>
                            </div>
                            <p><a href="http://movie.mtime.com/232758/trailer/70328.html" class="__r_c_" pan="M14_TheaterIndex_Upcoming_TrailerButton" target="_blank">预告片<i class="icon_ivideo"></i></a></p>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="232758" method="presell"></p>
                        </li>
                    </ul>
                </dd>
                <dd>
                    <ul>
                        <li><i class="dot">&nbsp;</i></li>
                        <li class="day"><strong>7月27日</strong>即将上映</li>
                        <li class="i_wantmovie"> 
                            <a href="http://movie.mtime.com/253688/" target="_blank" title="西虹市首富/Hello Mr.Millionaire(2018)" class="img __r_c_" pan="M14_TheaterIndex_Upcoming_Cover"><img src="http://img5.mtime.cn/mt/2017/12/15/151416.32507324_100X150X4.jpg" width="100" height="150" alt="西虹市首富/Hello Mr.Millionaire(2018)"></a>
                            <div class="__r_c_" pan="M14_TheaterIndex_Upcoming_Title">
                                <h3><a href="http://movie.mtime.com/253688/" target="_blank">西虹市首富</a></h3>
                                <p><span mid="253688" method="want" genre="1"></span><a href="http://movie.mtime.com/movie/search/section/?type=Comedy" target="_blank">喜剧</a></p>
                                <p class="i_wbr"><b>导演：</b><a href="http://people.mtime.com/2114123/" target="_blank">闫非</a> </p>
                            </div>
                            <p class="ticket __r_c_" pan="M14_TheaterIndex_Upcoming_TicketButton" mid="253688" method="presell"></p>
                        </li>
                    </ul>
                </dd>
            </dl>
        </div>
    </div>
</div>
        <div id="M14_B_TheaterChannelIndex_AboveCinemaTG"></div>         
<script type="text/javascript">
        var districtJson = [{"id":1380,"name":"集美区","bs":[{"bid":441,"bname":"杏林"}]}];
        var subwayJson = [];
        var cinemasJson = {"totalcount":40,"list":[{"cid":7458,"cname":"厦门博纳国际影城","logo":"http://img31.mtime.cn/t/2015/10/29/121103.62691945_102X63X3.jpg","sname":"厦门博纳国际影城","address":"厦门市思明区嘉禾路199号磐基二期中心4楼-6楼      ","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/7458/","feature":"{CinemaID:7458,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"总统式会员休息室\",Feature4D:0,Feature4DContent:\"\",Feature4DX:1,Feature4DXContent:\"\",FeatureHuge:1,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:1,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"烧鸟、FRESH&CHIP、壹制蛋糕\",FeatureFoodContent:\"三及第、东池便当、宾果每日、晋江牛肉、京城御面堂\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"优吉、SUNION、roseonly、MCM、ATTOS\",FeatureLeisureContent:\"见福、星巴克、许留山\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"\",Wifi:1,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":0},{"cid":5665,"cname":"厦门映联万和影城","logo":"http://img31.mtime.cn/t/2014/08/14/161445.92984011_102X63X3.jpg","sname":"厦门映联万和影城","address":"厦门市思明区七星西路3号乐都汇购物中心L3F011","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/5665/","feature":"{CinemaID:5665,Feature3D:1,Feature3DContent:\"采用墙对墙整壁式清晰金属银幕、BARCO数字放映机、高质音响设备，视听效果达到国际标准。\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"太平洋咖啡、麦当劳、大丰收、表妹靓点餐厅、桥亭活鱼小镇等等\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"乐购超市、健尔乐健身中心、屈臣氏、免费儿童游乐场等\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:2,GlassFor3DContent:\"3D眼镜3元/付，2付5元\",CardPay:1,CardPayContent:\"前台购票可刷卡付款\",Wifi:1,WIFIConent:\"影城内有免费wifi\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"商场配备有600多个免费地下停车位，从地下车库乘坐垂直电梯便可直接到达影城。\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":1,"lowestprice":"29"},{"cid":4664,"cname":"金逸影城MX4D（光美厦门五缘湾店）","logo":"http://img31.mtime.cn/t/2014/08/14/161431.61806699_102X63X3.jpg","sname":"金逸影城MX4D（光美厦门五..","address":"厦门市湖里区金湖路101号五缘湾乐都汇购物中心L4F007","did":1379,"dsname":"湖里区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Huli/4664/","feature":"{CinemaID:4664,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"四季大丰收、桥亭活鱼小镇、烤肉达人、田王府等。\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"宝乐迪KTV\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:2,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"商场免费停车\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":2,"lowestprice":"38"},{"cid":3850,"cname":"厦门明发金逸IMAX影城","logo":"http://img31.mtime.cn/t/2014/08/14/161310.33685995_102X63X3.jpg","sname":"厦门明发金逸IMAX影城","address":"厦门市思明区莲坂明发商业广场B区二楼百安居后侧","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/3850/","feature":"{CinemaID:3850,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:1,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"卖品部\",FeatureFoodContent:\"必胜客  燕江食府\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"售票柜台右边\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"地面及地下停车场0-4小时收费5元\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":3,"lowestprice":"34"},{"cid":3776,"cname":"厦门金逸海沧悦实店","logo":"http://img31.mtime.cn/t/2014/08/14/161301.73262573_102X63X3.jpg","sname":"厦门金逸海沧悦实店","address":"厦门市海沧区新阳街道新盛路19号悦实广场5号楼6层","did":2716,"dsname":"海沧区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_HaiCangQu/3776/","promotions":[],"sortid":4,"lowestprice":"34"},{"cid":2593,"cname":"金逸厦门文艺店","logo":"http://img31.mtime.cn/t/2014/08/14/161003.22769199_102X63X3.jpg","sname":"金逸厦门文艺店","address":"厦门体育路文化艺术中心科技馆一楼","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/2593/","feature":"{CinemaID:2593,Feature3D:1,Feature3DContent:\"1.2号厅配有300个座位，座椅排距为1.35米，双机3D系统，超大的金属银幕（15.4X6.6）\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"超五星级豪华贵宾VIP厅,配有40个座位,座椅均采用意大利真皮进口可调节式沙发\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"卖品部\",FeatureFoodContent:\"肯德基、大娘水饺、DQ冰雪皇后、康师傅牛肉面、味千拉面、雅子咖喱、牛芒绵绵冰等\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"大润发超市、工人体育馆、厦门科技馆、厦门图书馆、厦门博物馆等\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:2,GlassFor3DContent:\"1米3以下儿童（一位成人可带一位儿童，儿童无座）免费观影，但观看3D影片不提供3D眼镜\",CardPay:1,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"进门大厅右侧直走\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"凭2张电影票可以免费停车4小时\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":5,"lowestprice":"35"},{"cid":1817,"cname":"金逸影城厦门名汇全激光店","logo":"http://img31.mtime.cn/t/2014/08/14/160907.94706087_102X63X3.jpg","sname":"金逸影城厦门名汇全激光店","address":"厦门市霞溪路28号名汇广场三楼","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/1817/","feature":"{CinemaID:1817,Feature3D:0,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":6,"lowestprice":"29"},{"cid":1797,"cname":"金逸厦门明发店","logo":"http://img31.mtime.cn/t/2014/08/14/160906.30635165_102X63X3.jpg","sname":"金逸厦门明发店","address":"厦门市莲坂明发商业广场东区381号C区三楼","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/1797/","feature":"{CinemaID:1797,Feature3D:0,Feature3DContent:\"\",FeatureIMAX:1,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:0,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":7,"lowestprice":"34"},{"cid":9219,"cname":"首星巨幕影城（华美空间店）","logo":"http://img5.mtime.cn/t/2016/12/14/195401.53576307_102X63X3.jpg","sname":"首星巨幕影城（华美空间店）","address":"厦门市湖里区华昌路132号联发华美空间A2号楼","did":1379,"dsname":"湖里区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Huli/9219/","feature":"{CinemaID:9219,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:2,GlassFor3DContent:\"4月1日起，不再提供免费共享的3D眼镜\",CardPay:1,CardPayContent:\"\",Wifi:1,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:1,HallCustomPropertyName:\"激光厅\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":8,"lowestprice":"23"},{"cid":3942,"cname":"华彩中兴影城（原大地电影城）","logo":"http://img31.mtime.cn/t/2014/08/14/161319.52549049_102X63X3.jpg","sname":"华彩中兴影城（原大地电影..","address":"厦门市枋湖客运中心TBK商业中心二楼","did":1379,"dsname":"湖里区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Huli/3942/","feature":"{CinemaID:3942,Feature3D:1,Feature3DContent:\"金属银幕\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:1,FeatureGameContent:\"大型游戏厅就在楼下\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"KFC，麦当劳，蒸功夫，大娘水饺 \",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"TBK商业广场，永辉超市，珠宝\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"超大型停车场\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":9,"lowestprice":"28"},{"cid":8510,"cname":"厦门维宝国际影城（马巷店）","logo":"http://img31.mtime.cn/t/2016/04/29/114327.15513880_102X63X3.jpg","sname":"厦门维宝国际影城（马巷店）","address":"厦门市翔安区巷西一里4号","did":2718,"dsname":"翔安区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_XiangAnQu/8510/","feature":"{CinemaID:8510,Feature3D:1,Feature3DContent:\"全3D厅\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"\",Wifi:1,WIFIConent:\"进店关注微信公众号可用免费WiFi\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":10,"lowestprice":"35"},{"cid":2338,"cname":"厦门万达影城SM广场店","logo":"http://img31.mtime.cn/t/2014/08/14/160928.47966142_102X63X3.jpg","sname":"厦门万达影城SM广场店","address":"SM广场二期B座3层","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/2338/","feature":"{CinemaID:2338,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"卖品部\",FeatureFoodContent:\"大丰收鱼庄  仙踪林  汉堡王\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"SM新生活广场\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":11,"lowestprice":"38"},{"cid":2681,"cname":"厦门中影星美国际影城","logo":"http://img31.mtime.cn/t/2014/08/14/161008.52864652_102X63X3.jpg","sname":"厦门中影星美国际影城","address":"福建省厦门市思明区厦禾路899号罗宾森购物广场三楼","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/2681/","feature":"{CinemaID:2681,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"卖品部\",FeatureFoodContent:\"香港满记甜品，仙踪林，麦当劳，肯德基等等\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"大型购物商场，养生会所，KTV等等\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"影院大厅\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"数百个停车位\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":12,"lowestprice":"28"},{"cid":3026,"cname":"厦门湖里万达广场店","logo":"http://img31.mtime.cn/t/2014/08/14/161050.10537288_102X63X3.jpg","sname":"厦门湖里万达广场店","address":"厦门湖里区仙岳路4666号万达广场娱乐楼4层","did":1379,"dsname":"湖里区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Huli/3026/","feature":"{CinemaID:3026,Feature3D:1,Feature3DContent:\"Reald 3D 6FL厅数为8个\",FeatureIMAX:1,FeatureIMAXContent:\"IMAX厅12号厅295座IMAX身临其境的观影体验\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"豪华的设施配套\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:1,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"哈根达斯，爆米花，可乐等\",FeatureFoodContent:\"星巴克，国慧大酒楼，大丰收，黄鹤天厨等\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"大玩家，agogo KTV\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"银联；VISA；MasterCard；支付宝；Apple Pay；Samsung Pay\",Wifi:1,WIFIConent:\"WX-XMHLWDYC\",DisabledSeat:1,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"免费的地下停车场，停车数达2300个\",FeatureParkImageUrl:\"\",IsHallCustomProperty:1,HallCustomPropertyName:\"Real 3D 6FL厅\",HallCustomPropertyContent:\"6FL高亮度3D厅\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":13,"lowestprice":"38"},{"cid":2611,"cname":"中影数字梦工坊影城","logo":"http://img31.mtime.cn/t/2014/08/14/161004.17273256_102X63X3.jpg","sname":"中影数字梦工坊影城","address":"福建省厦门市思明区莲前东路123号加州城市广场4F东侧","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/2611/","feature":"{CinemaID:2611,Feature3D:1,Feature3DContent:\"设有情侣厅 氧吧厅\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:1,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"麦当劳，肯德基，大丰收，豪客来，鹿港小镇，味千拉面，日本料理，必胜客，加州美食广场\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"莱雅百货，沃尔玛，阿拉斯加真冰溜冰场，巴黎春天百货，欢唱，苏宁电器，如家快捷酒店\",Loveseat:1,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:1,GlassFor3DContent:\"3D眼镜需要自己购买\",CardPay:0,CardPayContent:\"\",Wifi:1,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"地下1000个免费停车位\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":14,"lowestprice":"38"},{"cid":4146,"cname":"厦门集美万达广场店","logo":"http://img31.mtime.cn/t/2014/08/14/161335.90158686_102X63X3.jpg","sname":"厦门集美万达广场店","address":"厦门市集美区银江路137号万达广场4层","did":1380,"dsname":"集美区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Jimei/4146/","feature":"{CinemaID:4146,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:1,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"万达广场三层大丰收、老知青、食汇堂等\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"万达广场三层大歌星、二层大玩家\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"万达广场地下停车场\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":15,"lowestprice":"33"},{"cid":2680,"cname":"完美世界影城中华城店（原17.5今典影城）","logo":"http://img5.mtime.cn/t/2017/08/10/115455.15949338_102X63X3.jpg","sname":"完美世界影城中华城店（原..","address":"福建省厦门市思明区思明南路195号中华城5楼","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/2680/","feature":"{CinemaID:2680,Feature3D:1,Feature3DContent:\"逼真效果，超乎想象！\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"尊荣独享，感受非凡！真皮可调节式沙发，舒适观影！\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"中华城美食城\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"巴黎春天，苏宁电器，老虎城购物中心，第一百货，麦当劳，肯德基 \",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"中华城地下停车场，拥有1000个停车位\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":16,"lowestprice":"37"},{"cid":2718,"cname":"中影国际影城厦门翔安店）","logo":"http://img31.mtime.cn/t/2014/08/14/161012.24620648_102X63X3.jpg","sname":"中影国际影城厦门翔安店）","address":"福建省厦门市翔安区汇景购物广场四楼","did":2718,"dsname":"翔安区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_XiangAnQu/2718/","feature":"{CinemaID:2718,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"西餐厅\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"KTV  酒店 文化中心\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"免费停车\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":17,"lowestprice":"39"},{"cid":8789,"cname":"厦门万达影城世茂海峡广场店","logo":"http://img31.mtime.cn/t/2016/07/28/160537.14051009_102X63X3.jpg","sname":"厦门万达影城世茂海峡广场店","address":"厦门市思明区演武西路世茂海峡大厦6楼","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/8789/","feature":"{CinemaID:8789,Feature3D:1,Feature3DContent:\"reald 3d\",FeatureIMAX:1,FeatureIMAXContent:\"IMAX厅配备：芝华士真皮沙发、情侣座\",FeatureIMAXHeight:22,FeatureIMAXWidth:12,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"大丰收、咏蛙田鸡、陶乡、鱼旨寿司等\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"休息区\",FeatureLeisureContent:\"康莱德酒店、X先生密室逃脱、世茂商场商铺\",Loveseat:1,LoveseatContent:\"IMAX厅拥有情侣座\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"\",Wifi:1,WIFIConent:\"有免费WiFi\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"影城大堂，扶梯左侧\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"商场总计1000余个停车位，暂不收费，后期费用由商管决定\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":18,"lowestprice":"32"},{"cid":1796,"cname":"厦门思明电影院","logo":"http://img31.mtime.cn/t/2014/08/14/160906.33251474_102X63X3.jpg","sname":"厦门思明电影院","address":"思明北路2号（思明南北路和思明东西路的十字路口）","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/1796/","feature":"{CinemaID:1796,Feature3D:1,Feature3DContent:\"XpanD3D系统。\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"临中山路多好吃地\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"中南商业广场地下车库、思明东西路右侧均可停车(停车费自付）。\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":19,"lowestprice":"38"},{"cid":5971,"cname":"中影梦工坊巨幕影城","logo":"http://img31.mtime.cn/t/2014/08/22/170601.64952793_102X63X3.jpg","sname":"中影梦工坊巨幕影城","address":"厦门市湖里区吕岭路蔡塘广场5楼","did":1379,"dsname":"湖里区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Huli/5971/","feature":"{CinemaID:5971,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:1,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:1,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:1,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:1,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:1,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:1,HallCustomPropertyName:\"DMAX\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":20,"lowestprice":"38"},{"cid":3785,"cname":"厦门完美世界影城集美店（原17.5影城）","logo":"http://img31.mtime.cn/t/2014/08/14/161302.25818628_102X63X3.jpg","sname":"厦门完美世界影城集美店（..","address":"厦门市集美区乐海路23号新华都商场3楼301号","did":1380,"dsname":"集美区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Jimei/3785/","feature":"{CinemaID:3785,Feature3D:0,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"渔家湾、盛世经典牛排、9527甜品店等\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"一楼服装商场；二楼大型新华都购物超市；三楼休闲娱乐：麦霸KTV、老房子足浴等。\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"配套400多个免费停车位，条件极其便利。\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":21,"lowestprice":"30"},{"cid":6671,"cname":"中影数字梦工坊影城（同安店）","logo":"http://img31.mtime.cn/t/2015/02/26/142440.65856702_102X63X3.jpg","sname":"中影数字梦工坊影城（同安..","address":"厦门市同安区环城西路乐海城市广场4楼","did":2717,"dsname":"同安区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_TongAnQu/6671/","feature":"{CinemaID:6671,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:1,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:1,FeatureGameContent:\"电玩城\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"麦当劳\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"屈臣氏、国美\",Loveseat:1,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:1,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"\",Wifi:1,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"免费\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":22,"lowestprice":"38"},{"cid":1107,"cname":"厦门中华电影院","logo":"http://img31.mtime.cn/t/2015/02/11/154924.84700879_102X63X3.jpg","sname":"厦门中华电影院","address":"厦门市思明区中山路219-225号","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/1107/","feature":"{CinemaID:1107,Feature3D:0,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:1,FeatureDolbyContent:\"1号厅配备杜比全景声\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"休闲咖啡座\",FeatureLeisureContent:\"中山路步行街\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:1,WIFIConent:\"百兆宽带\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:0,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:1,HallCustomPropertyName:\"时尚休闲咖啡座\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":23,"lowestprice":"39"},{"cid":9072,"cname":"厦门市奥斯卡国际影城","logo":"","sname":"厦门市奥斯卡国际影城","address":"福建省厦门市湖里区日圆二里1号建发湾悦城4楼（厦门市行政服务中心旁）","did":1379,"dsname":"湖里区","bid":"","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Huli/9072/","feature":"{CinemaID:9072,Feature3D:1,Feature3DContent:\"1,2,5,6,7,8号厅为普通3D厅\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"9,10号厅为VIP厅\",Feature4D:1,Feature4DContent:\"4D动感特效厅\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:1,FeatureHugeContent:\"3号厅巨幕厅\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:1,FeatureGameContent:\"暂无\",FeatureFood:1,FeatureFoodCinemaContent:\"可乐、饮料、爆米花、小食品\",FeatureFoodContent:\"潮福成、戏 锅、大 丰 收、咏蛙田鸡、汉堡王\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"大堂休息区\",FeatureLeisureContent:\"星巴克、太平洋、costa cafe\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:1,GlassFor3DContent:\" 3D眼镜售价3元/副\",CardPay:1,CardPayContent:\"可使用信用卡及储蓄卡（免手续费）\",Wifi:1,WIFIConent:\"暂无\",DisabledSeat:1,DisabledSeatContent:\"影城无障碍电梯、影厅设无障碍座椅、影院设无障碍卫生间\",SelfServiceTicket:1,SelfServiceTicketContent:\"大堂右侧\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"免费停车（以商场收费为准）\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":24,"lowestprice":"36"},{"cid":9031,"cname":"中影国际影城厦门金域华府万科里店","logo":"http://img5.mtime.cn/t/2016/10/18/183216.25561162_102X63X3.jpg","sname":"中影国际影城厦门金域华府..","address":"厦门市集美区杏林街道宁海一里64号三层L301铺位","did":1380,"dsname":"集美区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Jimei/9031/","feature":"{CinemaID:9031,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:1,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"3D眼镜免费提供使用，观影结束后归还\",CardPay:1,CardPayContent:\"\",Wifi:1,WIFIConent:\"影城提供免费WIFI\",DisabledSeat:1,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"商城停车场近225个停车位，凭当日影城观影票根可以在商场一楼客服台兑换停车券，免费停车4小时\",FeatureParkImageUrl:\"\",IsHallCustomProperty:1,HallCustomPropertyName:\"60帧影厅\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":25,"lowestprice":"47"},{"cid":9821,"cname":"星美国际影城厦门同安现代城店","logo":"","sname":"星美国际影城厦门同安现代..","address":" 福建省厦门市同安区工业集中区新景舜弘现代城3层3A商铺","did":2717,"dsname":"同安区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_TongAnQu/9821/","feature":"{CinemaID:9821,Feature3D:1,Feature3DContent:\"1.、2厅幕宽：8M 高：4.6M  3厅幕宽：10M  高4.6M\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"卖品区提供各类食品\",FeatureFoodContent:\"楼上楼夜宵城、KFC等\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"卖品休息区、大堂休息区\",FeatureLeisureContent:\"  \",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:1,GlassFor3DContent:\"10元\",CardPay:1,CardPayContent:\"可使用信用卡及储蓄卡（免手续费）\",Wifi:1,WIFIConent:\"免费提供50兆光纤Wifi\",DisabledSeat:1,DisabledSeatContent:\"影城无障碍电梯、影厅设无障碍座椅、影院设无障碍卫生间\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"凭影票可免费停车2小时\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":26,"lowestprice":"34"},{"cid":10144,"cname":"金逸影城厦门洋塘店","logo":"","sname":"金逸影城厦门洋塘店","address":"厦门市翔安区鼓锣一里61号119号闽篮城市广场三楼","did":2718,"dsname":"翔安区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_XiangAnQu/10144/","feature":"{CinemaID:10144,Feature3D:1,Feature3DContent:\"1.、2厅幕宽：8M 高：4.6M  3厅幕宽：10M  高4.6M\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"8号厅\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:1,FeatureDolbyContent:\"6号厅\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"卖品区提供各类食品\",FeatureFoodContent:\"楼上楼夜宵城、KFC等\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"卖品休息区、大堂休息区\",FeatureLeisureContent:\"\",Loveseat:1,LoveseatContent:\"1号厅\",GlassFor3D:1,GlassFor3DDeposit:1,GlassFor3DContent:\"10元\",CardPay:1,CardPayContent:\"可使用信用卡及储蓄卡（免手续费）可微信、支付宝支付\",Wifi:1,WIFIConent:\"免费提供50兆光纤Wifi\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"位于大堂\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"凭影票可免费停车4小时\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":27,"lowestprice":"38"},{"cid":6281,"cname":"星美国际影城厦门禹洲店","logo":"http://img31.mtime.cn/t/2015/04/21/095927.91373148_102X63X3.jpg","sname":"星美国际影城厦门禹洲店","address":"厦门市海沧区兴港路167号2-3层","did":2716,"dsname":"海沧区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_HaiCangQu/6281/","promotions":[],"sortid":28,"lowestprice":"29"},{"cid":2067,"cname":"梦露歌剧院影城","logo":"http://img31.mtime.cn/t/2014/08/14/160917.52009258_102X63X3.jpg","sname":"梦露歌剧院影城","address":"厦门海沧阿罗海城市广场（区政府旁）","did":2716,"dsname":"海沧区","bid":"0","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_HaiCangQu/2067/","feature":"{CinemaID:2067,Feature3D:1,Feature3DContent:\"所有影厅均具备3D功能。\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"歌剧院主题设计，2个主题情侣厅等个性化影厅。\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:1,FeatureGameContent:\"ET电玩城\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"肯德基，麦当劳，星巴克，豪客来，豪享来，必胜客、大丰收、老知青\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"梦幻都市ktv\",Loveseat:1,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:1,GlassFor3DContent:\"免费借用5元押金/副、购票套餐免费赠送（新3D眼镜）\",CardPay:1,CardPayContent:\"\",Wifi:1,WIFIConent:\"\",DisabledSeat:1,DisabledSeatContent:\"\",SelfServiceTicket:1,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"购买套餐赠送停车券（3D眼镜/停车券2选1）\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":29},{"cid":2405,"cname":"厦门世纪嘉华电影院","logo":"http://img31.mtime.cn/t/2014/08/14/160937.28176370_102X63X3.jpg","sname":"厦门世纪嘉华电影院","address":"厦门市集美区建南路3号（杏东青少年宫广场）","did":1380,"dsname":"集美区","bid":"441","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Jimei/2405/","feature":"{CinemaID:2405,Feature3D:0,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:0,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":30},{"cid":8675,"cname":"中影数字圣谛影城","logo":"http://img31.mtime.cn/t/2016/06/21/143830.25178212_102X63X3.jpg","sname":"中影数字圣谛影城","address":"福建省厦门市思明区厦禾路888号","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/8675/","feature":"{CinemaID:8675,Feature3D:0,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"配有真皮豪华可调节航空座椅，并配备有USB接口为手机充电\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:1,FeatureDolbyContent:\"美国杜比DOLBY-CP750数字解码器、美国QSC功放系统，美国JBL扬声器等\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"湘阁里辣、肯德基、麦当劳、汉堡王、咏蛙田鸡、海底捞、星巴克、哈根达斯等等\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"金榜公园、世贸商城\",Loveseat:1,LoveseatContent:\"为广大热恋中的情侣配备了双人无间隔沙发座椅，让观影情侣们享受温馨幸福的两人世界\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"可支持微信支付、信用卡支付\",Wifi:1,WIFIConent:\"禹洲·世贸商城、中影数字圣谛影城全WIFI全覆盖\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:0,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":31},{"cid":1988,"cname":"同安影剧院","logo":"http://img31.mtime.cn/t/2014/08/14/160913.69153285_102X63X3.jpg","sname":"同安影剧院","address":"同安区环城南路985号(文体中心体育馆东侧)","did":2717,"dsname":"同安区","bid":"0","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_TongAnQu/1988/","feature":"{CinemaID:1988,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"竹林雅舍，阿瓦山寨\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"芭乐KTV，糖果KTV\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"停车休闲广场，地下停车场可以容纳近千辆车\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":32},{"cid":1362,"cname":"厦门世贸金鹰电影院","logo":"http://img31.mtime.cn/t/2014/08/14/160839.26502560_102X63X3.jpg","sname":"厦门世贸金鹰电影院","address":"厦禾路888号世贸商城五楼","did":1381,"dsname":"思明区","bid":"0","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Siming/1362/","feature":"{CinemaID:1362,Feature3D:1,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:0,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":33},{"cid":9616,"cname":"大地影院-厦门国贸美岁天地","logo":"","sname":"大地影院-厦门国贸美岁天地","address":"福建省厦门市集美区凤林路26号美岁天地4楼","did":1380,"dsname":"集美区","bid":"0","sbid":"","sid":"","isticket":true,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Jimei/9616/","feature":"{CinemaID:9616,Feature3D:1,Feature3DContent:\"2号-7号为巴克4k高清影厅\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:1,Feature4DContent:\"8号为MX4厅\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:1,Feature4KContent:\"1-8号均为4K设备\",FeatureDolby:1,FeatureDolbyContent:\"1号星幕厅为激光杜比全景声厅\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"卖品区提供各类食品\",FeatureFoodContent:\"味友，星巴克，汉堡王\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"简餐区\",FeatureLeisureContent:\"宝乐迪KTV、大润发超市\",Loveseat:1,LoveseatContent:\"7号为情侣厅\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"刷微信和支付宝\",Wifi:1,WIFIConent:\"免费提供50兆光纤Wifi\",DisabledSeat:1,DisabledSeatContent:\"影城无障碍电梯、影厅设无障碍座椅、影院设无障碍卫生间\",SelfServiceTicket:1,SelfServiceTicketContent:\"集美区凤林路26号国贸美岁天地4楼嘉庚体育馆后50米\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"凭影票可免费停车6小时\",FeatureParkImageUrl:\"\",IsHallCustomProperty:1,HallCustomPropertyName:\"1号为大地自有品牌22米宽STAR MAX星幕厅\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":34,"lowestprice":"33"},{"cid":3049,"cname":"厦金湾汽车电影院","logo":"","sname":"厦金湾汽车电影院","address":"厦门市湖里区环岛东路五通社区厦金湾海滨旅游休闲区厦金湾汽车文化有限公司","did":1379,"dsname":"湖里区","bid":"0","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Huli/3049/","promotions":[],"sortid":35},{"cid":10119,"cname":"厦门泰和影城","logo":"","sname":"厦门泰和影城","address":"厦门闽南古镇","did":1379,"dsname":"湖里区","bid":"0","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Huli/10119/","promotions":[],"sortid":36},{"cid":1498,"cname":"长宏影剧院","logo":"","sname":"长宏影剧院","address":"厦门市集美杏林杏西路消防大队对面","did":1380,"dsname":"集美区","bid":"441","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Jimei/1498/","feature":"{CinemaID:1498,Feature3D:0,Feature3DContent:\"\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:0,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"\",FeatureLeisure:0,FeatureLeisureCinemaContent:\"\",FeatureLeisureContent:\"\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:0,CardPayContent:\"\",Wifi:0,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:0,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":37},{"cid":6648,"cname":"厦门喀秋莎影城","logo":"http://img31.mtime.cn/t/2015/02/10/113025.58772465_102X63X3.jpg","sname":"厦门喀秋莎影城","address":"厦门市集美文教区后勤服务中心E座二楼天马路313号","did":1380,"dsname":"集美区","bid":"0","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen_Jimei/6648/","feature":"{CinemaID:6648,Feature3D:1,Feature3DContent:\"4个影厅（1号厅、2号厅、3号厅、4号厅）声道居屏3D影厅\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:0,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:0,Feature4KContent:\"\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:1,FeatureGameContent:\"伊斯贝尔网咖 位于厦门市集美天马路旺角学生商业街313号2楼\",FeatureFood:1,FeatureFoodCinemaContent:\"\",FeatureFoodContent:\"德克士、黄鹤楼、宴火阑珊、转转乐，位于旺角学生商业街\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"网咖 、ktv\",FeatureLeisureContent:\"台球馆\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:0,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"\",Wifi:1,WIFIConent:\"\",DisabledSeat:1,DisabledSeatContent:\"影院有残疾通道\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"免费\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":38},{"cid":8255,"cname":"厦门沃奇乐影城（即将开业）","logo":"http://img31.mtime.cn/t/2016/01/21/134343.87012331_102X63X3.jpg","sname":"厦门沃奇乐影城（即将开业）","address":"厦门市湖里区长浩东路27号5楼B5栋","did":0,"dsname":"","bid":"","sbid":"","sid":"","isticket":false,"showtimepage":"http://theater.mtime.com/China_Fujian_Province_Xiamen/8255/","feature":"{CinemaID:8255,Feature3D:1,Feature3DContent:\"影厅装潢独具特色，影厅搭配不同的花色座椅，与影厅背景相结合\",FeatureIMAX:0,FeatureIMAXContent:\"\",FeatureIMAXHeight:0,FeatureIMAXWidth:0,FeatureVIP:1,FeatureVIPContent:\"\",Feature4D:0,Feature4DContent:\"\",Feature4DX:0,Feature4DXContent:\"\",FeatureHuge:0,FeatureHugeContent:\"\",Feature4K:1,Feature4KContent:\"1号巨幕厅搭配巴可4K双机设备\",FeatureDolby:0,FeatureDolbyContent:\"\",FeatureGame:0,FeatureGameContent:\"\",FeatureFood:1,FeatureFoodCinemaContent:\"牛皇叔烤肉、云鼎汇砂养生砂锅、慕瑟咖啡吧等\",FeatureFoodContent:\"台湾正宗夜市小吃、国内知名餐饮\",FeatureLeisure:1,FeatureLeisureCinemaContent:\"影城四楼为电影主题馆，设有电影主题餐厅、衍生品超市、游戏互动体验区等\",FeatureLeisureContent:\"台湾酷奇宝乐园\",Loveseat:0,LoveseatContent:\"\",GlassFor3D:1,GlassFor3DDeposit:0,GlassFor3DContent:\"\",CardPay:1,CardPayContent:\"\",Wifi:1,WIFIConent:\"\",DisabledSeat:0,DisabledSeatContent:\"\",SelfServiceTicket:0,SelfServiceTicketContent:\"\",SelfServiceTicketImageUrl:\"\",FeaturePark:1,FeatureParkContent:\"\",FeatureParkImageUrl:\"\",IsHallCustomProperty:0,HallCustomPropertyName:\"\",HallCustomPropertyContent:\"\",IsServiceCustomProperty:0,ServiceCustomPropertyName:\"\",ServiceCustomPropertyContent:\"\"}","promotions":[],"sortid":39}]};
        var appQRcodeSrc = "http://service.mtime.com/GetQrCodeHandler.ashx?qrCodeStr=http://feature.mtime.com/mobile/";
</script>

<div class="newshowtime filmticket">
   		<div class="title clearfix">
        	<h2 class="fl">厦门<span>40</span>家影院</h2>
            <div class="othermenu ">
                     <ul class="clearfix othertab">
                        <li id="areaAndSubwayFilter" class="first __r_c_" pan="M14_TheaterIndex_Cinema_Business">商圈及地铁沿线 <i class="ico_f_jiao">&nbsp;</i><em>&nbsp;</em></li>
                        <li id="featureFilter" class="__r_c_" pan="M14_TheaterIndex_Cinema_Version">
                            <i class="ico_radio notcheck" v="1"></i><label class="v_m notcheck" v="1">购票</label>
                            <i class="ico_radio notcheck" v="2"></i><label class="v_m notcheck" v="2">停车场</label> 
                            <i class="ico_radio notcheck" v="3"></i><label class="v_m notcheck" v="3">3D</label>
                            <i class="ico_radio notcheck" v="4"></i><label class="v_m notcheck" v="4">IMAX</label>
                            <i class="ico_radio notcheck" v="5"></i><label class="v_m notcheck" v="5">4DX</label>
                        </li>
                     </ul>
                     <div class="citysearch __r_c_" pan="M14_TheaterIndex_Cinema_Search">
                        <input id="inputCinameKeyword" type="text" class="text" value="搜索影院" />
                        <input id="buttonCinameKeyword" type="button" class="button" />
                     </div>
                     <dl id="cinemaSearchTip" class="showsearch searchcity __r_c_" pan="M14_TheaterIndex_Cinema_Search" style="display:none;">
                     </dl>
                     <div id="areaAndSubwayfilterBox" class="showcitybox clearfix __r_c_" pan="M14_TheaterIndex_Cinema_Business" style="display:none;top:43px;left:185px;">
                     </div>
                  </div>
        </div>
        
        <div data-selector="cinemas" class="clearfix filmticketbox">
        	<div class="main fl">
            	<div class="movietxt">
                     <ul id="cinemaListRegion" class="__r_c_" pan="M14_TheaterIndex_Cinema_List">
                     <div class="movielogin"><div class="load104"><i class="loadimg">&nbsp;</i><i class="logo"></i></div></div>
                     </ul>
                </div>
                <div class="i_more" style="display:none;"><a id="morecinema" href="#" onclick="return false;"><i></i>更多</a></div>
            </div>
            <div class="aside fr">
                
                <div id="M14_B_TheaterChannelIndex_RightTG1"></div>
                
                
                <div id="M14_B_TheaterChannelIndex_RightTG2"></div>
            </div>
        </div>
        
   </div>        <div id="M14_B_TheaterChannelIndex_FooterTG"></div>    <div class="filmtip">
      <div class="filmtipbox">
         <ul class="clearfix">
            <li class="first">
            <a href="http://piao.mtime.com" target="_blank" class="c_333" style="text-decoration:none">
               <div class="moviecard">
                  <div class="cardbg"></div>
                  <div class="cardbg1"></div>
                  <dl>
                     <dt>时光电影卡：</dt>
                     <dd>尊享3－6折优惠，支持在线选座</dd>
                     <dd>企业个性化定制</dd>
                     <dd>商务馈赠，节日送礼，员工福利</dd>
                  </dl>
               </div>
               </a>
 </li>

            <li>
               <div class="ticketoline">
                  <h2>如何在线选座购票：</h2>
                  <p></p>
               </div>
                
            </li>
            <li class="last telbox"> <span class="fr tel"><b>客服电话：</b>4006-118-118</span> <b>影院商务合作：</b> <a href="http://theater.mtime.com/report/1" target="_blank">影院开业</a> <span class="mline">｜</span> <a href="http://theater.mtime.com/report/4/" target="_blank">影讯合作</a> <span class="mline">｜</span> <a href="http://theater.mtime.com/report/2/" target="_blank">在线购票</a> <span class="mline">｜</span> <a href="http://theater.mtime.com/report/1/" target="_blank" class="link_green">联系时光网</a> </li>
         </ul>
      </div>
       
   </div></div><script type="text/javascript">
					if ( typeof(mtimeStufs) == "undefined" ) {
							 mtimeStufs = [];
					}
mtimeStufs.push( {id:"M14_B_TheaterChannelIndex_AboveHotplayTG",type:"mtime",content:"<div class=\"tc \" style=\"height:70px; position:relative; width:1000px; margin:0 auto;\">\n<div style=\"position: absolute;  height:90px; left:0; top:12px;\">\n<iframe  src=\"http://static1.mtime.cn/tg/2011/2014_theater_hotshowing_banner_1000x90.html\" width=\"1000\" height=\"90\" frameborder=\"0\" border=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\" allowtransparency=\"true\"></iframe>\n</div></div>\n"} );
mtimeStufs.push( {id:"M14_B_TheaterChannelIndex_FooterTG",type:"mtime",content:"<div class=\"tc  pb15\">\n<iframe  src=\"http://static1.mtime.cn/tg/2011/2014_theater_footer_banner_1000x90.html\" width=\"1000\" height=\"90\" frameborder=\"0\" border=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\" allowtransparency=\"true\"></iframe>\n</div>"} );
mtimeStufs.push( {id:"M14_B_TheaterChannelIndex_RightTG2",type:"mtime",content:"<div class=\"mt15 mb15\">\n<iframe  src=\"http://static1.mtime.cn/tg/2011/2014_theater_square_up_300x250.html\" width=\"300\" height=\"250\" frameborder=\"0\" border=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\" allowtransparency=\"true\"></iframe>\n</div>\n"} );
</script>     <a id="udesk-im-61" href="javascript:;" title="联系客服" >联系客服</a>
<style type="text/css">
#udesk-im-61{ background:url(http://static1.mtime.cn/feature/2016/kefu.jpg?04271506) no-repeat 0 0; width::50px; height:50px; display:block; font-size:0; line-height:0; border-radius:3px 0 0 3px;opacity:.9;filter: alpha(opacity=90);}
#udesk-im-61:hover{ background-position:0 -50px;opacity:1;filter: alpha(opacity=100);}
.movietxt .movieinfobox .infotxt .moretool{width:420px;}
</style>
<script>
			
window.onload = function() {
  var myADTimer;

  function setIntervalADTimer() {
    var mtimebarbox = document.getElementsByClassName("searchbar")[0];
    if (mtimebarbox) {
      var mtimeserverbox = document.getElementById('udesk-im-61');
      mtimebarbox.parentNode.insertBefore(mtimeserverbox, mtimebarbox);
      mtimeserverbox.onclick = function() { window.open("http://www.mtime.udesk.cn/im_client?cur_url=" + encodeURIComponent(location.href) + "&pre_url=" + encodeURIComponent(document.referrer), "udesk_im", "width=780,height=560,top=200,left=350,resizable=yes"); };
      myADTimer && clearTimeout(myADTimer);
    } else {
      myADTimer = setTimeout(function() {
        setIntervalADTimer();
      }, 2000);
    }
  }

  setIntervalADTimer();
};

</script><script type="text/javascript">    topMenuValues.mainNavPage = 3; //影院</script><div id="bottom"></div>
<script type="text/javascript">  document.write(unescape("%3Cscript src='" + jsServer + "/js/systemall2014.js' type='text/javascript'%3E%3C/script%3E"));</script>
<script type="text/javascript">  document.write(unescape("%3Cscript src='" + subJsServer + "/js/cinemapagepack.js' type='text/javascript'%3E%3C/script%3E"));</script>
<script type="text/javascript">
	//页尾 导航
	//  静态文件初始化类
	new StaticManager({
	});
</script>
<div style="display: none">
	<script type="text/javascript">
		var tracker = new Tracker();
		tracker.trackPageView();
	</script>
</div>
	<script type="text/javascript">	</script>    <script type="text/javascript">    $loadSubJs("/js/2014/channel/cinemachannelpage.js", function () {         new CinemaChannelPage({cityId:323});    });</script></body></html>
<!--Generated at 2018-5-3 11:40:13 by Mtime Staticize Service.--><!--complie:107 ms-->'''

    a = HtmlParser()
    b = a.parser_url('http://movie.mtime.com/',r)
    print(b)
    print(len(b))

