const orderDirect=(direction)=>{
    let newURL = '';
    let currentURL=window.location.pathname;
    if(direction==='view'){
        if(currentURL.search('sort')===-1){
            currentURL+='sort=views';
        }
        else{}
    }
    else if(direction==='date'){}
    else{}
}
/*
const movePage = function(page) {
  const URLSearch = new URLSearchParams(location.search);
  URLSearch.set('page', String(page));
  const newParam = URLSearch.toString();

  window.open(location.pathname + '?' + newParam, '_self');
};
*/