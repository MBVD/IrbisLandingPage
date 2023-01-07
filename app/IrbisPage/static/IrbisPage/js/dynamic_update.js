const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add("show")
            entry.target.classList.remove("hidden")
        }
    })
})
$('.hidden').each(function(id, el){
    console.log(el)
    observer.observe(el)
})  