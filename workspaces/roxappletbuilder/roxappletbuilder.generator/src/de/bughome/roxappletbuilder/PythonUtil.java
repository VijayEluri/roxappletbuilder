package de.bughome.roxappletbuilder;

import java.util.ArrayList;
import java.util.List;

public final class PythonUtil {
	
	private PythonUtil(){
		throw new IllegalStateException();
	}
	
    public static String getUID(final Object o){
        final int uid = System.identityHashCode(o);
        
        return Integer.toHexString(uid);
    }

    public static String multiply(final String s, final Long factor){
		final int factorInt = factor.intValue();
		
		if(factor == 0) return "";
		if(factor == 1) return s;
		
		final StringBuilder sb = new StringBuilder(s.length() * factorInt);
		for(int i = 0; i < factorInt; ++i){
			sb.append(s);
		}
		
		return sb.toString();
	}
    
    public static List<String> getPackages(final String p){
    	final String[] packageNames = p.split("[.]");
    	
    	final List<String> subPackages =
    		new ArrayList<String>(packageNames.length + 1);
    	subPackages.add("");
    	
    	final StringBuilder sb = new StringBuilder(p.length());
    	for(int i = 0; i < packageNames.length; ++i){
    		if(i > 0){
    			sb.append(".");
    		}
    		
    		sb.append(packageNames[i]);
    		
    		subPackages.add(sb.toString());
    	}
    	
    	return subPackages;
    }

}
