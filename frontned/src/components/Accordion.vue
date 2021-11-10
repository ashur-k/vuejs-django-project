<template>
    <div class="accordin">
        <button 
            type="button" 
            id='accordin__button' 
            class="accordin__button">Expand Content</button>
        <div class="accordion__content">
            <p>
               Some text
            </p>
        </div>
    </div>   
</template>
<script>
export default {
  name: "Accordion",
  props: {
    
  },
  mounted(){
    this.getAccordion()
  },
  methods: {
    getAccordion(){
      console.log('funcs wonks')
      const button = document.getElementById('accordin__button');
       
          button.addEventListener('click', () => {
              console.log("Buton")
            const accordinContent = button.nextElementSibling;
            button.classList.toggle('accordin__button--active');
            if (button.classList.contains('accordin__button--active')){
              accordinContent.style.maxHeight = accordinContent.scrollHeight + 'px'
            } else {
              accordinContent.style.maxHeight = 0;
            }
          });
      }
  },
    
};
</script>



<style>
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