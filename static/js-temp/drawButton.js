const drawButton = function () {
  const sections = ["정치", "경제", "사회", "생활/문화", "IT/과학", "세계"];
  const themes = ["정치", "경제", "사회", "생활", "IT", "세계"];
  const buttonStyle = ["home-button-change-option", "button-theme"];
  let container = document.getElementById("sectionButtons");

  const buttonDraw = function () {
    console.log("drawed");
    container.insertAdjacentHTML(
      "beforeend",
      drawMainButton() + drawSectionButton()
    );
  };
  const buttonSet = function () {
    let searchParams = new URLSearchParams(location.search);
    let viewRange = document.getElementById("viewRange");
    document.getElementById(searchParams.get("theme")).className =
      "button-theme-clicked section-button";
    viewRange.value = searchParams.get("number");
    document.getElementById("rangeValue").innerText = viewRange.value;
    return console.log("setted");
  };
  const drawMainButton = function () {
    let mainButton =
      window.location.pathname === "/"
        ? `<button type='button' class=${buttonStyle[0]} id='mainButton' value='/sections'>주제별 뉴스</button>`
        : `<button type='button' class=${buttonStyle[0]} id='mainButton' value='/'>전체 뉴스</button>`;
    return mainButton;
  };
  const drawSectionButton = function () {
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

  return {
    buttonDraw: buttonDraw,
    buttonSet: buttonSet,
  };
};

export default drawButton;
