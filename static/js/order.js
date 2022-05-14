const orderDirect=(direction)=>{
    let currentPath=window.location.pathname;
    let isExist=currentPath.search('sort');
    if(isExist===-1)
       currentPath+='?sort='+direction;
    else
        currentPath+='&sort='+direction;
    window.location.href=currentPath;
}
