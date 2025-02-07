/*
    NAME:          popup.js
    AUTHOR:        Alan Davies (Lecturer Health Data Science)
    EMAIL:         alan.davies-2@manchester.ac.uk
    DATE:          18/12/2019
    INSTITUTION:   University of Manchester (FBMH)
    DESCRIPTION:   JavaScript file for managing display of popup dialoges
*/

function Popup()
{
    var popup = new Object();
    popup.mask = document.getElementById("page-mask");
    popup.entryFormPopup = document.getElementById("creat-calc");
    popup.aboutPopup = document.getElementById("about-box");
    popup.datasourcesPopup = document.getElementById("datasources-box");
    popup.bnfcodesPopup = document.getElementById("bnfcodes-box");
    popup.faqPopup = document.getElementById("faq-box");


    // display the popup mask
    popup.showMask = function()
    {
        this.mask.style.display = "block";
        $('#page-mask').height($(document).height());
    }

    //hide the popup mask
    popup.hideMask = function()
    {
        this.mask.style.display = "none";
    }

    //show the creatinine clearance calculator form dialog
    popup.showCeatCalcFormPopup = function()
    {
        this.showMask();
        this.entryFormPopup.style.display = "block";
        this.positionDialogue(this.entryFormPopup);
        //this.entryFormPopup.style.left = (($(document).width() / 2) - (this.entryFormPopup.offsetWidth / 2)) + "px";
    }

    // hide the creatinine clearance calculator form dialog
    popup.hideCeatCalcFormPopup = function()
    {
        this.hideMask();
        this.entryFormPopup.style.display = "none";
    }

    // show the about popup
    popup.showAboutPopup = function()
    {
        this.showMask();
        this.aboutPopup.style.display = "block";
        this.positionDialogue(this.aboutPopup);
    }

    // hide about popup
    popup.hideAboutPopup = function()
    {
        this.hideMask();
        this.aboutPopup.style.display = "none";
    }

    // show the data sources popup
    popup.showdatasourcesPopup = function()
    {
        this.showMask();
        this.datasourcesPopup.style.display = "block";
        this.positionDialogue(this.datasourcesPopup);
    }

    // hide data sources popup
    popup.hidedatasourcesPopup = function()
    {
        this.hideMask();
        this.datasourcesPopup.style.display = "none";
    }

     // show the bnf codes popup
     popup.showbnfcodesPopup = function()
     {
         this.showMask();
         this.bnfcodesPopup.style.display = "block";
         this.positionDialogue(this.bnfcodesPopup);
     }
 
     // hide bnf codes popup
     popup.hidebnfcodesPopup = function()
     {
         this.hideMask();
         this.bnfcodesPopup.style.display = "none";
     }

     // show the faq popup
     popup.showfaqPopup = function()
     {
         this.showMask();
         this.faqPopup.style.display = "block";
         this.positionDialogue(this.faqPopup);
     }
 
     // hide faq popup
     popup.hidefaqPopup = function()
     {
         this.hideMask();
         this.faqPopup.style.display = "none";
     }
 
    // position dialogue center screen
    popup.positionDialogue = function(popupBox)
    {
    popupBox.style.left = (($(document).width() / 2) - (popupBox.offsetWidth / 2)) + "px";
    }

    return popup;
}