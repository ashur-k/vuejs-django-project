<template>
  <div class="home">
    <section class="hero-section bg-light">
      <div class="hero-heading text-center">
        <p class="title">Wild Child Animation</p>
        <p class="">WCA IT SUPPORT SECTION</p>
      </div>
    </section>
 

    <div class="">
      <div class="col-sm-12">
        <h2 class="mt-5 text-end">IT FLOOR LAYOUT</h2>
      </div>
  
      <div 
        class="col-sm-12 table"
        v-for="table in tables"
        v-bind:key="table.id"
        >
         
          <div class="">
             <h3 class="p-2 m-5">{{ table.friendly_name }}</h3>
             <hr>
            <div 
              class="box has-text-centered computer-node" 
              style=""
              v-for="(computer, index) in table.computer_details"
              v-bind:key="computer.id" >
              <div class="accordion" id='computer'>
                <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                    <button 
                      class="accordion-button" 
                      type="button" 
                      data-bs-toggle="collapse" 
                      :data-bs-target="'#computer'+index" 
                      aria-expanded="true" 
                      aria-controls="collapseOne">
                      Computer Informaiton
                    </button>
                  </h2>
                  <div :id="'computer'+index" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                  <div class="accordion-body">
                    <ul class="list-group">
                      <li class="list-group-item">
                        <strong>Machine title -</strong>
                        {{computer.machine_title}}
                      </li>
                      <li class="list-group-item">
                        <strong>Machine IP -</strong>
                        {{computer.machine_ip_address}}</li>
                      <li class="list-group-item">
                        <strong>Machine OS -</strong>
                        {{computer.machine_os}}</li>
                      <li class="list-group-item">
                        <strong>Machine GPU's -</strong>
                        {{computer.numbers_of_gpu}}</li>
                    </ul> 
                  </div>
                  </div>
                </div>
              

      </div>
                           
              <h3 class="is-size-4">{{ computer.machine_title }}</h3>
            </div>
              
          </div>
         
       
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "Home",
  data() {
    return{
      tables: []
    }
  },
  components: {
   
  },
  mounted(){
    this.getComputers(),
    this.getAccordion()
  },
  methods: {
    getComputers(){
      axios.get('/api/v1/computers-layout/')
      .then(response => {
        this.tables = response.data
        console.log(this.tables)
      })
      .catch(error => {
        console.error(error)
      })
      console.log(':bringi accordion in getcom')
    },
    getAccordion(){
      console.log('funcs wonks')
        document.querySelectorAll('.accordin__button').forEach(button => {
          button.addEventListener('click', () => {
            const accordinContent = button.nextElementSibling;
            button.classList.toggle('accordin__button--active');
            if (button.classList.contains('accordin__button--active')){
              accordinContent.style.maxHeight = accordinContent.scrollHeight + 'px'
            } else {
              accordinContent.style.maxHeight = 0;
            }
          });
        });
      }
  },
    
};
</script>
<style>
.hero-section{
  align-items: stretch;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.hero-heading{
  padding: 3rem 3rem;
}
  .table{
    display: flex;
    flex-direction: column;
    float: right;
    border-top: 2px solid currentColor !important;
  }
  .computer-node{
    width: 33.3%; 
    float:right; 
    height:100%; 
    margin:10px;
    background-color: #4a4a4a;
    color: #ffffff;
  }
  .accordin__button{
    display: block;
    width: 100%;
    padding: 15px;
    border: none;
    outline: none;
    cursor: pointer;
    background: #4a4a4a;
    color: #ffffff;
    text-align: left;
    transition: background 0.2s;
  }
  .accordin__button::after{
    content: '\25be';
    float: right;
    transform: scale(1.5);
  }
  .accordin__button--active  {
    background: #555555;
  }
  .accordin__button--active::after  {
    content: '\25ba';
  }
  .accordion__content{
    overflow: hidden;
    max-height: 0;
    transition: max-height 0.2s;

    padding: 0 15px;
    background: #eeeeee;
  }
</style>
