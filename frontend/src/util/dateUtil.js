export function dateUtil() {
  function showDate(date) {
    const d = new Date(date)
    const year = d.getFullYear()
    const month = String(d.getMonth() + 1).padStart(2, '0') // 월은 0부터 시작하므로 +1
    const day = String(d.getDate()).padStart(2, '0')
    return `${year}-${month}-${day}`
  }
  function totalDay() {
    const days = []
    const daysInMonth = 31
    for (let i = 1; i <= daysInMonth; i++) {
      days.push(i)
    }
    return days
  }
  return { showDate, totalDay }
}
