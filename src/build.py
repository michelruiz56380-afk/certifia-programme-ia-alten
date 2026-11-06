import base64,sys,re
# usage: build.py [unlock]
d='/mnt/project-files/formation-alten/programme/'
t=open(d+'src/programme.tpl.html').read()
b=lambda f:'data:image/png;base64,'+base64.b64encode(open(d+'src/'+f,'rb').read()).decode()
t=t.replace('{{LOGO_WHITE}}',b('logo_allwhite_s.png')).replace('{{LOGO_NAVY}}',b('logo_navy_s.png')).replace('{{LOGO_ALTEN}}',b('logo_alten_s.png'))
suffix=''
if len(sys.argv)>1 and sys.argv[1]=='unlock':
    url='https://drive.google.com/drive/folders/10XhqX-a20_cSJB_5sAhnJrvbOM-3HUen?usp=sharing'
    t=re.sub(r'<div class="lockbanner" id="lockbanner">.*?</div>',
      '<div class="lockbanner open" id="lockbanner"><span>Les supports sont en ligne. <a href="'+url+'" target="_blank" rel="noopener"><b>Ouvrir le dossier des supports (Google Drive)</b></a></span></div>',t,flags=re.S)
    t=t.replace('<span>Disponible le 19/11</span>','<span>Dans le dossier Drive</span>').replace('Module bonus, non présenté en séance · 19/11','Module bonus, non présenté en séance').replace('doc locked','doc')
    suffix='_supports'
open(d+'src/artifact_programme'+suffix+'.html','w').write(t)
head,rest=t.split('<header',1)
open(d+('src/' if suffix else '')+'Programme_Formation_IA_Alten'+suffix+'.html','w').write('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+head+'</head>\n<body>\n<header'+rest+'\n</body>\n</html>\n')
