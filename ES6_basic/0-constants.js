export function taskFirst() {
    const task = 'I prefer const when I can.'; //const can never be modified
    return task;
}
  
export function getLast() {
    return ' is okay';
}
  
export function taskNext() {
    let combination = 'But sometimes let'; //can be modified outside this block
    combination += getLast();
  
    return combination;
}
