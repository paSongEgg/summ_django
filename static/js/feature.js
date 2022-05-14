/*전역 변수*/
var themes=['정치','경제','사회','생활','IT','세계'];
var clickedButton=localStorage.getItem("clicked");
var currentLODvalue='전체';
window.onload=()=>{
    makeSectionButtons();
    var tmp=new URLSearchParams(location.search);
    document.getElementById('viewRange').value=tmp.get('number');
    document.getElementById('rangeValue').innerText=document.getElementById('viewRange').value;
    switch(tmp.get('number')){
        case '0':document.getElementById("news_table").style.fontSize="1em";break;
        case '1':document.getElementById("news_table").style.fontSize="1.1em";break;
        case '2':document.getElementById("news_table").style.fontSize="1em";break;
        case '3':document.getElementById("news_table").style.fontSize="0.9em";break;
        case '4':document.getElementById("news_table").style.fontSize="0.8em";break;
        case '5':document.getElementById("news_table").style.fontSize="0.7em";break;
    }
    switch(tmp.get('theme')){
        case '정치':document.getElementById("정치").className="button-theme-clicked";break;
        case '경제':document.getElementById("경제").className="button-theme-clicked";break;
        case '사회':document.getElementById("사회").className="button-theme-clicked";break;
        case '생활':document.getElementById("생활").className="button-theme-clicked";break;
        case 'IT':document.getElementById("IT").className="button-theme-clicked";break;
        case '세계':document.getElementById("세계").className="button-theme-clicked";break;
    }
}
/*페이지 이동 버튼 조정하는 함수*/
function makeSectionButtons(){
    let container=document.getElementById("sectionButtons");
    let mainButton=document.createElement('button');
    let sections=['정치','경제','사회','생활/문화','IT/과학','세계'];
    mainButton.className="home-button-change-option";
    mainButton.type="button";
    if(window.location.pathname.substring(0,2)!=='/s'){
        mainButton.innerText="주제별 뉴스";
    }
    else{
        mainButton.innerText="전체 뉴스"
    }
    mainButton.addEventListener('click',(e)=>{
        let currentPath=window.location.pathname;
        console.log(currentPath.substring(0,2));
        if(currentPath.substring(0,2)==='/s'){
            currentPath='/';
        }
        else {
            currentPath='/sections';
        }
        window.location.href=currentPath;
    });
    container.appendChild(mainButton);
    for(var i=0;i<6;i++){
        let sectionButton=document.createElement('button');
        sectionButton.addEventListener('click',(e)=>sendSectionValue(e));
        sectionButton.value=themes[i];
        sectionButton.className="button-theme";
        sectionButton.id=themes[i];
        sectionButton.innerText=sections[i];
        sectionButton.type="button";
        container.appendChild(sectionButton);

    }
}

function sendSectionValue(e){
    let currentPath=window.location.pathname;
    let sectionValue=e.target.value;
    let i=0;
    for(i=0;i<6;i++){
        if(e.target.value===themes[i]) {
            localStorage.setItem("clicked",i);
            break;
        }
    }
    if(i===6)localStorage.removeItem("clicked");
    if(currentPath==='/') currentPath+='sections?';
    
    else if(currentPath==='/sections'){
        currentPath+='?';
    }
    else {
        currentPath+='&';
    }
    currentPath+='theme='+sectionValue;
    window.location.href=currentPath;
}

/*LOD 조정 버튼을 생성하는 함수*/
function rangeChange(event){
    let currentPath=window.location.pathname;
    var tmp=new URLSearchParams(location.search);
    tmp.set('number',event.target.value);
    window.location.href=currentPath+'?'+tmp.toString();
}

function sendLodValue(e){
    let currentPath=window.location.pathname;
    let lodValue=e.target.value;
    if(currentPath==='/'||currentPath==='/sections'){
        currentPath+='?';
    }
    else {
        currentPath+='&';
    }
    currentPath+='number='+lodValue;
    window.location.href=currentPath;
}

function changeSort(e){
    let currentPath=window.location.pathname;
    let sortValue=e.target.value;
    if(currentPath==='/'||currentPath==='/sections'){
        currentPath+='?';
    }
    else {
        currentPath+='&';
    }
    currentPath+='sort='+sortValue;
    window.location.href=currentPath;
}

const showList=(list)=>{
    console.log(list);
}
function openNews(e){
    console.log(e);
    location.href=e.target.innerText;
}