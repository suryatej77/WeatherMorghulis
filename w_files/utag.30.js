//tealium universal tag - utag.30 ut4.0.201604291824, Copyright 2016 Tealium.com Inc. All Rights Reserved.
window.googletag=window.googletag||{};googletag.cmd=googletag.cmd||[];if(typeof utag.ut=="undefined"){utag.ut={};}
utag.ut.libloader2=function(o,a,b,c,l){a=document;b=a.createElement('script');b.language='javascript';b.type='text/javascript';b.async=true;b.src=o.src;if(o.id){b.id=o.id}
if(typeof o.cb=='function'){b.hFlag=0;b.onreadystatechange=function(){if((this.readyState=='complete'||this.readyState=='loaded')&&!b.hFlag){b.hFlag=1;o.cb();}};b.onload=function(){if(!b.hFlag){b.hFlag=1;o.cb();}};}
l=o.loc||'head';c=a.getElementsByTagName(l)[0];if(c){if(l=='script'){c.parentNode.insertBefore(b,c);}else{c.appendChild(b);}
utag.DB("Attach to "+l+": "+o.src);}};try{(function(id,loader,u){try{u=utag.o[loader].sender[id]={}}catch(e){u=utag.sender[id]};u.ev={'view':1};u.qsp_delim="&";u.kvp_delim="=";u.divid="";u.slot="";u.height="";u.width="";u.collapseEmptyDivs="true";u.base_url="https://www.googletagservices.com/tag/js/gpt.js";u.map={"ad_bidding":"setTargeting","ad_placements":"gptSlots","preempt":"preempt","ad_unit":"adunit","ads_test":"adstest","site":"site","barometer":"baro","city":"ct","claritas":"cid","condition":"cnd","country_code":"cc","day_of_week":"dow","dma":"dma","entry":"ent","exclude":"excl","forecast_day_1":"fc1","forecast_day_2":"fc2","forecast_day_3":"fc3","forecast_high_increment":"fhi","forecast_high_range":"fhr","forecast_low_increment":"fli","forecast_low_range":"flr","humidity":"hmid","language":"lang","locale":"locale","meta_refresh":"mr","page_view":"vw","pollen":"plln","severe":"sev","quantcast":"qct","state":"st","temperature":"tmp","temperature_range":"tmpr","twc_location_id":"loc","twc_page":"twcpage","zip_code":"zip","layout":"lo","platform":"plat","time_frame":"tf","wundermap_layers":"mlayer","programmatic_group":"pg","tpid":"tpid","weather_fx":"wfxtg","weather_fx_zcs":"zcs","weather_fx_hzcs":"hzcs","weather_fx_nzcs":"nzcs","lotame_audience":"sg","browser_type":"browser"};u.extend=[];u.send=function(a,b,c,d,e,f){if(u.ev[a]||typeof u.ev.all!="undefined"){u.setTargeting={};for(d in utag.loader.GV(u.map)){if(typeof b[d]!="undefined"&&b[d]!=""){e=u.map[d].split(",");for(f=0;f<e.length;f++){if(e[f]=="slot"||e[f]=="gptSlots"||e[f]=="height"||e[f]=="width"||e[f]=="collapseEmptyDivs"||e[f]=="setTargeting_slot"||e[f]=="setTargeting"){u[e[f]]=b[d]}else{u.setTargeting[e[f]]=b[d]}}}}
u.myCallback2=function(){u.initialized=true;if(u.networkcode&&u.adunit){u.slot="/"+u.networkcode+"/"+u.adunit;}
u.gptSlots=u.gptSlots||((u.width===""&&u.height==="")?[[u.slot,null,u.divid]]:[[u.slot,[parseInt(u.width),parseInt(u.height)],u.divid]]);googletag.cmd.push(function(){for(f=0;f<u.gptSlots.length;f++){var slot;if(u.gptSlots[f][1]==null||u.gptSlots[f][1]=="OutOfPageSlot"){slot=googletag.defineOutOfPageSlot.apply(this,[u.gptSlots[f][0],u.gptSlots[f][2]]).addService(googletag.pubads());}else{slot=googletag.defineSlot.apply(this,u.gptSlots[f].slice(0,3)).addService(googletag.pubads());}
var data=u.gptSlots[f][3]||u.setTargeting_slot||{};for(d in data){slot.setTargeting(d+'',data[d])}
if(u.collapseEmptyDivs=="true"){slot.setCollapseEmptyDiv(true);}
if(typeof index_headertag_lightspeed!=='undefined'){index_headertag_lightspeed.addDFPSlot(slot);}
}
googletag.pubads().enableSingleRequest();googletag.enableServices();});googletag.cmd.push(function(){for(f in u.setTargeting){googletag.pubads().setTargeting(f,u.setTargeting[f]);}
function displaySlots(utagSlots){for(var j=0;j<utagSlots.length;j++){if(document.getElementById(utagSlots[j][2])){googletag.display(utagSlots[j][2]);}}}
if(typeof index_headertag_lightspeed!=='undefined'){var cb=(function(utagSlots,dfpSlots){return function(){index_headertag_lightspeed.set_slot_targeting(dfpSlots);displaySlots(utagSlots);};}(u.gptSlots,index_headertag_lightspeed.getDFPSlots()));index_headertag_lightspeed.envoke_on_or_after_session_end(cb,true);}
else{displaySlots(u.gptSlots);}
});};u.myCallback=function(){utag.ut.libloader2({src:"//ox-d.weatherus.servedbyopenx.com/w/1.0/jstag?nc=7646-wunderground",cb:u.myCallback2});};if(!u.initialized){utag.ut.libloader2({src:"https://www.googletagservices.com/tag/js/gpt.js",cb:u.myCallback});}else{u.myCallback();}}}
try{utag.o[loader].loader.LOAD(id)}catch(e){utag.loader.LOAD(id)}})('30','weather.wunderground');}catch(e){}