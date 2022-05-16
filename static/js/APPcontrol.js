import drawButton from "./drawButton.js";
const APPcontrol = ((drawBtn) => {
  const setPage = () => {
    drawBtn.draw();
    drawBtn.set();
    addClickEvent();
  };
  const addClickEvent = () => {
    let sectionButton = document.getElementsByClassName("section-button");
    let sortButton=document.getElementsByClassName('news-table-click');

    document.getElementById("mainButton").addEventListener("click", (e) => {
      window.location.href = e.target.value;
    });
    /*수정할 것*/
    sectionButton.map((button) =>
      button.addEventListener("click", (e) => {
        let currenParam=new URLSearchParams(location.search);
        let section=currenParam.set('theme',e.target.value);
        window.location.href = `${window.loction.pathname}?${currentParam/toString()}`;
      })
    );
    sortButton.map((button)=>
      button.addEventListener("click",(e)=>{
        let currenParam=new URLSearchParams(location.search);
        let sort=currenParam.set('sort',direction);
        window.location.href=`${window.location.pathname}?${currenParam.toString()}`;
      }))
  };
  
  return {
    setPage();
  };
})(drawButton);

APPcontrol.setPage();
