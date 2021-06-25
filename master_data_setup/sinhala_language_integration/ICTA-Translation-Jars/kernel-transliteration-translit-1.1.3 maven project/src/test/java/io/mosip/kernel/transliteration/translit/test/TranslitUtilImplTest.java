package io.mosip.kernel.transliteration.translit.test;


import static org.hamcrest.CoreMatchers.isA;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;

import io.mosip.kernel.transliteration.translit.impl.TranslitUtilImpl;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import io.mosip.kernel.core.transliteration.exception.InvalidTransliterationException;
import io.mosip.kernel.core.transliteration.spi.Transliteration;

/**
 * This Unit test class contains test methods for SL transliteration engine
 */
@SpringBootTest(classes = {TranslitUtilImpl.class})
@RunWith(SpringRunner.class)
public class TranslitUtilImplTest {

    /**
     *
     * Key for sinhala language.
     */
    @Value("${sinhala-language-code}")
    private String sinhalaLanguageCode;

    /**
     * Key for tamil language.
     */
    @Value("${tamil-language-code}")
    private String tamilLanguageCode;

    /**
     * Reference to {@link Transliteration}.
     */
    @Autowired
    private Transliteration<String> translitUtilImpl;

    /**
     * This method test successfull transliteration of provided string as mention by
     * language code.
     */
    @Test
    public void transliterateTest() {

        String sinhalaToTamilOutput = translitUtilImpl.transliterate(sinhalaLanguageCode, tamilLanguageCode, "සාදරයෙන් පිළිගනිමු");

        assertThat(sinhalaToTamilOutput, isA(String.class));
        assertEquals("சாதரயென் பிளிகனிமு", sinhalaToTamilOutput);

    }

    /**
     * This method test for invalid input language code provided by user.
     */
    @Test(expected = InvalidTransliterationException.class)
    public void transliterateInvalidInputLanguageCodeExceptionTest() {
        translitUtilImpl.transliterate("dnjksd", "sin", "Bienvenue");
    }

    /**
     * This method test for invalid target language code provided by user.
     */
    @Test(expected = InvalidTransliterationException.class)
    public void transliterateInvalidOutputLanguageCodeExceptionTest() {
        translitUtilImpl.transliterate("eng", "aradkn", "Bienvenue");
    }
}
