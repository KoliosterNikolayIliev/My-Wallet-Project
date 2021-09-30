import React from "react";
import MailchimpFormContainer from "./MailChimpFormContainer";
// here you can import all other components you need

const LandingPage = () => {
  return (
    <main>
      <header>
        <div class="header">
            <p>Managing your investments should be trivial</p>
        </div>
        <div class="description">
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestias aut, repellat ipsum facere voluptate dicta obcaecati deserunt nobis suscipit eaque?</p>
        </div>
      </header>

        <div>
          <MailchimpFormContainer />
        </div>

        <article class="message">
          <p>
            Join the <strong>824</strong> people that have signed up for our early January launch.
          </p>
          <p>
            Only 5.000 spots available!
          </p>
        </article>


        <article>
          <div class="container">
          <div class="row">
            <div class="col-sm-6">
              <div class="sub-title">Text goes here!</div>
              <span class="more-info">
              <p>Proident aute dolor aliquip eu. Irure voluptate officia deserunt mollit. Incididunt velit in est officia elit ea consequat ea cillum dolor fugiat.</p>
              <p>Ullamco est enim et non proident consequat. Do magna pariatur ea mollit esse adipisicing ipsum ad esse dolor. Occaecat ullamco elit pariatur nostrud incididunt ipsum in eiusmod velit laborum cillum deserunt magna. Consectetur laborum in exercitation elit ipsum enim. Eiusmod veniam proident ad culpa excepteur pariatur excepteur nulla dolor pariatur irure magna eu labore. Proident anim laboris in elit laboris veniam.</p></span>
            </div>

            <div class="col-sm-2">
              <img src="/images/image-woman.jpg"></img>
            </div>

            </div>
          </div>
        </article>

        <article>
        <div class="container">
          <div class="row">
              <div class="col-sm-6">
              <img src="/images/image-people.jpg"></img>
            </div>


            <div class="col-sm-6">
              <div class="sub-title">Text goes here!</div>
              <span class="more-info">
              <p>Proident aute dolor aliquip eu. Irure voluptate officia deserunt mollit. Incididunt velit in est officia elit ea consequat ea cillum dolor fugiat.</p>
              <p>Ullamco est enim et non proident consequat. Do magna pariatur ea mollit esse adipisicing ipsum ad esse dolor. Occaecat ullamco elit pariatur nostrud incididunt ipsum in eiusmod velit laborum cillum deserunt magna. Consectetur laborum in exercitation elit ipsum enim. Eiusmod veniam proident ad culpa excepteur pariatur excepteur nulla dolor pariatur irure magna eu labore. Proident anim laboris in elit laboris veniam.</p></span>
            </div>


            </div>
          </div>
        </article>


        <article>
          <div class="container">
          <div class="row">
            <div class="col-sm-6">
            <div class="sub-title">Text goes here!</div>
              <span class="more-info">
              <p>Proident aute dolor aliquip eu. Irure voluptate officia deserunt mollit. Incididunt velit in est officia elit ea consequat ea cillum dolor fugiat.</p>
              <p>Ullamco est enim et non proident consequat. Do magna pariatur ea mollit esse adipisicing ipsum ad esse dolor. Occaecat ullamco elit pariatur nostrud incididunt ipsum in eiusmod velit laborum cillum deserunt magna. Consectetur laborum in exercitation elit ipsum enim. Eiusmod veniam proident ad culpa excepteur pariatur excepteur nulla dolor pariatur irure magna eu labore. Proident anim laboris in elit laboris veniam.</p></span>
            </div>

            <div class="col-sm-2">
              <img src="/images/image-woman-second.jpg"></img>
            </div>

            </div>
          </div>
        </article>


        <article>
        <div>
          <MailchimpFormContainer />
        </div>
        </article>


    <article>
      <p>
        <hr/>
        Copyright @2021
      </p>
    </article>

    </main>

    

  );
};

export default LandingPage;
