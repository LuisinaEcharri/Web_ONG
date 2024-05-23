<?php
// Leer los datos del archivo JSON
$json_data = file_get_contents('datos.json');

// Decodificar los datos JSON a un array asociativo
$data = json_decode($json_data, true);
?>

<!doctype html>
<html lang="es" itemscope itemtype="http://schema.org/WebPage">
<head>
    <title>Reinventar Tandil</title>
    <link rel="icon" href="../favicon.ico">
    <!-- general meta data -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">    
    <meta name=robots content="index,follow">    
    <meta name="description" content="Reinventar Tandil es una Asociación Civil sin fines de lucro, no gubernamental.">
    <meta name="keywords" content="Reinventar Tandil, Reinventar, Tandil, ONG, Asociación Civil, Hockey">
    <meta name="author" content="Reinventar Tandil">
    <link rel="canonical" href="http://www.reinventartandil.com/">
    <meta name="subject" content="Reinventar Tandil">
    <meta name='Classification' content='ONG'>
    <meta name='url' content='http://www.reinventartandil.com/ '>
    <meta http-equiv='Expires' content='0'>
    <meta http-equiv='Pragma' content='no-cache'>
    <meta http-equiv='Cache-Control' content='no-cache'>
    <meta http-equiv='imagetoolbar' content='no'>
    <meta http-equiv='x-dns-prefetch-control' content='off'>    
    <!-- Open Graph data http://ogp.me/ -->
    <meta property="og:title" content="Reinventar Tandil" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="http://www.reinventartandil.com/" />
    <meta property="og:image" content="http://reinventartandil.com/Welcome2.jpg" />
    <meta property="og:image:type" content="image/jpeg">
    <meta property="og:description" content="Reinventar Tandil es una Asociación Civil sin fines de lucro, no gubernamental.">
    <meta property="og:site_name" content="Reinventar Tandil" />

    <!-- JQUERY-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>

    <!-- FONTS FAMILY -->
    <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Nunito+Sans:wght@700&family=Red+Hat+Display&display=swap" rel="stylesheet">
    <style> @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Nunito+Sans:wght@700&family=Red+Hat+Display&display=swap'); </style>
	
    <!-- CSS -->
    <link rel="stylesheet" href="./carousel_news.css">
    <link href="../css/bootstrap.css" rel="stylesheet" type="text/css" media="all" />
    <link rel="stylesheet" href="../css/variables.css">
    <link rel="stylesheet" href="../css/navbar.css">
    <link rel="stylesheet" href="../css/footer.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link  rel="stylesheet"  href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>


    <!-- FONT AWESOME -->
    <script src="https://kit.fontawesome.com/c5d8d8beeb.js" crossorigin="anonymous"></script>
    
</head>
<body>
    <!-- NAVIGATION -->
    <nav class="navbar" itemprop="breadcrumb" itemscope itemtype="https://schema.org/BreadcrumbList">
        <ul class="navbar_menu">
          <li class="navbar_logo" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem"><a href="../index.html#" itemprop="item"><img src="../img/logo.png" alt="logo" id="navbar_logo"/></a></li>
          <li class="navbar_item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem"><a href="../index.html#us" itemprop="item">QUIÉNES SOMOS</a></li>
          <li class="navbar_item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem"><a href="../index.html#activities" itemprop="item">ACTIVIDADES</a></li>
          <li class="navbar_item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem"><a href="./news.html#news" itemprop="item">NOTICIAS</a></li>
          <!--TODO Ver que hacer con hace un donativo!!-->
          <li class="navbar_item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem"><a class="navbar_donate_button" data-toggle="modal" data-target="#exampleModal" itemprop="item">HACÉ UN DONATIVO AHORA</a></li>
          
          <li class="navbar_item navbar_button" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem"><a class="navbar_contact_button" href="../index.html#contactUS" itemprop="item">CONTACTANOS</a></li>
          <li class="navbar_toggle" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem"><a href="#" itemprop="item"><i class="fas fa-bars"></i></a></li>
        </ul>
      </nav>

    <!-- CAROUSEL NEWS-->

    <section id="news" class="news">
        <!--
        <h2><span class="news_underline">Not</span>icias</h2>
        -->
        <!-- Slider main container -->
        <div class="swiper">
            <!-- Additional required wrapper -->
            <div class="swiper-wrapper">
                <!-- Slides -->
                <?php if (!empty($data)): ?>

                    <tbody>
                        <?php foreach ($data as $row): ?>
                            <div class="swiper-slide">
                                <!-- News-->
                                <article class="sub_main_news_carousel">
                                    <img class="up_sub_main_news_img" src="<?php echo  htmlspecialchars($row['imagen']) ?>"  alt="<?php echo  htmlspecialchars($row['imagen']) ?>">
                                    <div class="bottom_sub_main_news_text_container">
                                        <div class="epigrafe">
                                            <?php echo $row['epigrafe'] ?>
                                        </div>
                                        <div class="sub_main_news_title">
                                            <?php echo $row['titulo'] ?>
                                        </div> 
                                        <div class="news_text sub_main_news_text">
                                            <?php echo $row['cuerpo'] ?>
                                        </div>
                                    </div>
                                </article>
                            </div>
                            <!--
                            <tr>
                                <?php foreach ($row as $cell): ?>
                                    <td><?php echo htmlspecialchars($cell); ?></td>
                                <?php endforeach; ?>
                            </tr>
                            -->
                        <?php endforeach; ?>
                    </tbody>
                <?php else: ?>
                    <p>No se encontraron resultados.</p>
                <?php endif; ?>

            </div>
            <!-- If we need pagination -->
            <div class="swiper-pagination"></div>
        
            <!-- If we need navigation buttons -->
            <div class="swiper-button-prev"></div>
            <div class="swiper-button-next"></div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="footer">
        <div class="footer_first_section">
            <div class="footer_first_section_right">
                <img class="footer_reinventar_logo" src="../img/logo_footer.png" itemscope itemtype=https://schema.org/ImageObject alt="Intelifaz Logo"></img> 
            </div>
            <div class="footer_social_media">
                <p>Seguinos</p>
                <a class="footer_social_media_anchor" href="https://www.facebook.com/reinventar.tandil" target="_blank"><img class="footer_social_media_logo" src="../img/facebook_logo.png" itemscope itemtype=https://schema.org/ImageObject alt="Reinventar Facebook"></img></a>
                <a class="footer_social_media_anchor" href="https://www.instagram.com/reinventartandil/" target="_blank"><img class="footer_social_media_logo" src="../img/instagram_logo.png" itemscope itemtype=https://schema.org/ImageObject alt="Reinventar Instagram"></img></a>
                <a class="footer_social_media_anchor" href="https://wa.me/5492494489835?text=Hola! me comunicaba para" target="_blank"><img class="footer_social_media_logo_wa" src="../img/whatsapp_logo2.png" itemscope itemtype=https://schema.org/ImageObject alt="Reinventar Whatsapp"></img></a>
            </div>
        </div>
        <p class="footer_separator"></p>
        <div class="footer_second_section">
            <p class="footer_copyright">©2005-23 Reinventar. Todos los derechos reservados.</p>
            <div class="footer_intelifaz">
                <p class="footer_credits">El diseño de este sitio fue posible gracias a</p>
                <a class="footer_intelifaz_anchor" href="http://www.intelifaz.com" target="_blank"><img class="footer_intelifaz_logo" src="../img/intelifaz.png" itemscope itemtype=https://schema.org/ImageObject alt="Intelifaz Logo"></img></a>
            </div>
        </div>
    </footer> 

    

    <script src="../js/navbar.js"></script>
    <script src="../js/contact.js"></script>
    <script src="../js/jquery.min.js"></script>
	<script src="../js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script src="./swiper.js"></script>


</body>    
</html>
