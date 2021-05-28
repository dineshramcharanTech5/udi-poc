package io.mosip.kernel.transliteration.translit.impl;

import com.asankha.translit.Transliterate;
import io.mosip.kernel.core.transliteration.exception.InvalidTransliterationException;
import io.mosip.kernel.core.transliteration.spi.Transliteration;
import io.mosip.kernel.transliteration.translit.constant.LanguageIdConstant;
import io.mosip.kernel.transliteration.translit.constant.TransliterationErrorConstant;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.util.HashMap;
import java.util.Map;

@Component
public class TranslitUtilImpl implements Transliteration<String> {

    private static final String ENG_LOCALE = "eng";

    /**
     *
     * Key for Sinhala language.
     */
    @Value("${sinhala-language-code}")
    private String sinhalaLanguageCode;

    /**
     * Key for Tamil language.
     */
    @Value("${tamil-language-code}")
    private String tamilLanguageCode;

    Map<String, Integer> languageIdMap;


    @PostConstruct
    private void getLanguageMap() {

        languageIdMap = new HashMap<>();

        languageIdMap.put(ENG_LOCALE, Transliterate.ENGLISH);
        languageIdMap.put(sinhalaLanguageCode, LanguageIdConstant.SINHALA.getLanguage());
        languageIdMap.put(tamilLanguageCode, LanguageIdConstant.TAMIL.getLanguage());
    }

    @Override
    public String transliterate(String fromLanguage, String toLanguage, String inputText) {
        Integer srcLocaleCode = languageIdMap.get(fromLanguage);
        Integer targetLocaleCode = languageIdMap.get(toLanguage);

        if (srcLocaleCode == null || targetLocaleCode == null) {
            throw new InvalidTransliterationException(
                    TransliterationErrorConstant.TRANSLITERATION_INVALID_LANGUAGE_CODE.getErrorCode(),
                    TransliterationErrorConstant.TRANSLITERATION_INVALID_LANGUAGE_CODE.getErrorMessage());
        }

        String transliteratedResult = "";

        try {
            transliteratedResult = Transliterate.translateWord(inputText, srcLocaleCode, targetLocaleCode, Transliterate.UNKNOWN);
            transliteratedResult = processInputText(inputText, transliteratedResult);
        } catch (Exception ex) {
            throw new InvalidTransliterationException(
                    TransliterationErrorConstant.TRANSLITERATION_INVALID_ID.getErrorCode(),
                    TransliterationErrorConstant.TRANSLITERATION_INVALID_ID.getErrorMessage(), ex);
        }
        return transliteratedResult;
    }

    private String processInputText (String input_text, String transliterated_text) {
        String result = processLeading_I(input_text, transliterated_text);
        result = process_KA(input_text, result);
        result = process_LLA(input_text, result);

        return  result;
    }

    private String processLeading_I(String in, String out){
        String result = out;

        if( in.charAt(0) == '\u0B87' && in.charAt(1) == '\u0BB0'){
            result = out.substring (1, out.length());
        }
        return result;
    }

    private String process_KA(String in, String out){
        String result = out;
        char temp [] = in.toCharArray();

        for(int i =0; i < temp.length; i++){
            if(temp[i] == '\u0B95' && i>0 && temp[i+1]!='\u0BCD' && temp[i-1]!=' ' && temp[i-1]!='\u0BCD' ){
                result = result.replace('\u0DC4', '\u0D9C');
            }
        }
        return result;
    }

    private String process_LLA(String in, String out){
        String result = out;
        char temp [] = in.toCharArray();

        for(int i =0; i < temp.length; i++){
            if(temp[i] == '\u0BB3'){
                result = result.replace('\u0DC5', '\u0DBD');
            }
        }
        return result;
    }
}
