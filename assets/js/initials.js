document.addEventListener('DOMContentLoaded', async () => {
  const paragraph = document.querySelector('#initial-paragraph')
  if (!paragraph) return

  const initial = paragraph.innerText.trim().substring(0, 1)
  if (!initial.match(/[A-Z]/)) return

  const baseurl = document.documentElement.dataset.baseurl || ''
  const path = `${baseurl}/assets/initials/${initial.toLowerCase()}.svg`

  try {
    const response = await fetch(path)
    if (!response.ok) return
    const svgText = await response.text()

    paragraph.innerHTML = `
      <span class="initial-svg">${svgText}</span>
      ${paragraph.innerHTML.replace(/^\s*(\w)/, '<span class="hidden">$1</span>')}
    `
  } catch (error) {
    console.error('Error loading initial:', error)
  }
})
