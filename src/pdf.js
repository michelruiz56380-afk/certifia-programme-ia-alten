const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:900}});
await p.goto('file:///mnt/project-files/formation-alten/programme/Programme_Formation_IA_Alten.html',{waitUntil:'networkidle'});
console.log(await p.evaluate(()=>document.fonts.check('16px Urbanist')));
await p.screenshot({path:'/tmp/desk_unused.png',fullPage:false});
await p.pdf({path:'/mnt/project-files/formation-alten/programme/Programme_Formation_IA_Alten.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close();})();
