<?php 

	declare(strict_types=1);
	use PHPUnit\Framework\TestCase;

    final class ExampleTest extends TestCase{
    	
        public function testSumar(){

            $num1 = 1;
            $num2 = 1;
            $this->assertSame(2, $num1+$num2);
        }
    }


?>
