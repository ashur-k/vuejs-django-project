<template>
  <div id="wrapper">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <router-link to="/" class="navbar-brand">
            <strong>WCA</strong>
          </router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link to="/layout" class="nav-link active" aria-current="page">Layout</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/inventory" class="nav-link active" aria-current="page">Inventory</router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    
    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered"> Copyright (c) 2021</p>
    </footer>
  
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    }
  }
}
</script>


<style>
/* @import "../node_modules/bulma/css/bulma.css"; */
</style>
