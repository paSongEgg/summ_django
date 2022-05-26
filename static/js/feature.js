const sections = ["정치", "경제", "사회", "생활/문화", "IT/과학", "세계"];
const themes = ["정치", "경제", "사회", "생활", "IT", "세계"];
const buttonStyle = ["home-button-change-option", "button-theme"];
let container = document.getElementById("sectionButtons");

const drawMainButton = () => {
  let mainButton =
    window.location.pathname === "/"
      ? `<button type='button' class=${buttonStyle[0]} id='mainButton' value='/sections'>주제별 뉴스</button>`
      : `<button type='button' class=${buttonStyle[0]} id='mainButton' value='/'>전체 뉴스</button>`;
  return mainButton;
};
const drawSectionButton = () => {
  let sectionButton = "";
  for (var i = 0; i < 6; i++)
    sectionButton += `
              <button 
                  type='button' 
                  class='${buttonStyle[1]}  section-button' 
                  value=${themes[i]} 
                  id=${themes[i]}
              >${sections[i]}
              </button>
          `;
  return sectionButton;
};
const buttonDraw = () => {
  container.insertAdjacentHTML(
    "beforeend",
    drawMainButton() + drawSectionButton()
  );
};
const buttonSet = () => {
  let searchParams = new URLSearchParams(location.search);
  let viewRange = document.getElementById("viewRange");
  if (searchParams.get("theme") !== null) {
    document.getElementById(searchParams.get("theme")).className =
      "button-theme-clicked section-button";
    viewRange.value = searchParams.get("number");
    document.getElementById("rangeValue").innerText = viewRange.value;
  }
};

const APPcontrol = () => {
  const setPage = () => {
    buttonDraw();
    buttonSet();
    addClickEvent();
  };
  const addClickEvent = function () {
    let sectionButton = document.getElementsByClassName("section-button");
    let sortButton = document.getElementsByClassName("news-table-click");

    document.getElementById("mainButton").addEventListener("click", (e) => {
      window.location.href = e.target.value;
    });
    Array.prototype.forEach.call(sectionButton, function (button) {
      button.addEventListener("click", (e) => {
        let currentParam = new URLSearchParams(location.search);
        currentParam.set("theme", e.target.value);
        window.location.href = `${
          window.location.pathname
        }?${currentParam.toString()}`;
      });
    });
    Array.prototype.forEach.call(sortButton, function (button) {
      button.addEventListener("click", (e) => {
        let currentParam = new URLSearchParams(location.search);
        currentParam.set("sort", e.target.getAttribute("value"));
        window.location.href = `${
          window.location.pathname
        }?${currentParam.toString()}`;
      });
    });
  };
  return setPage();
};

const rangeChange = (event) => {
  let currentPath = window.location.pathname;
  var tmp = new URLSearchParams(location.search);
  tmp.set("number", event.target.value);
  window.location.href = currentPath + "?" + tmp.toString();
};
APPcontrol();
