import com.apama.util.Logger;
import com.apama.epl.plugin.annotation.EPLPlugin;
import com.apama.jmon.annotation.Application;

@Application(name = "TestPluginApplication",
		   author = "",
			version = "1.0",
			company = "Software AG",
			description = "Sample plugin for testing that the builder image works",
			classpath = "")


@EPLPlugin()
public class TestPlugin
{
	public static String getString() { return "Hello World"; }
}
