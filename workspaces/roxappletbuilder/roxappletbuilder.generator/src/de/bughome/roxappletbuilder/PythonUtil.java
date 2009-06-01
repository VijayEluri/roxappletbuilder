package de.bughome.roxappletbuilder;

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

}
