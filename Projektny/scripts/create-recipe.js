function handleRecipeSubmit(event) {
  event.preventDefault();
  
  const data = new FormData(event.target);
  
  const formToJSON = Object.fromEntries(data.entries());

  /* sparad onödig kod:
  formJSON.snacks = data.getAll('snacks'); */
  
  /*
  Här borde vi kalla en function med AJAX - POST till API (om vi haft ett API)
  Istället sparas vårt recept till att visas under 'Mina Recept', som JSON objekt (JSON.stringify)
  */

  const finishedRecipe = document.querySelector('.recipes');
  finishedRecipe.innerText = JSON.stringify(formToJSON, null, 2);
}

// skapar recipeForm - från html elementet med class recipe-form
// och lägger en EventListener på submit - då kallas handRecipeSubmit
const recipeForm = document.querySelector('.recipe-form');
recipeForm.addEventListener('submit', handleRecipeSubmit);