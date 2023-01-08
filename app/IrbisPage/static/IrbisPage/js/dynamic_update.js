const observer = new IntersectionObserver((entries) => {
    var isBefore = true
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add("show")
            entry.target.classList.remove("hidden")
            isBefore = false
        }
        if (isBefore){
            entry.target.style.transform = "translateX(0)"
        }
    })
})
$('.hidden').each(function(id, el){
    observer.observe(el)
    // if (is_before){
    //     console.log(el)
    //     el.style.transform = "translateX(0)"
    // }
})