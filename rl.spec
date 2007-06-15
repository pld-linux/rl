Summary:	A command-line tool
Summary(pl.UTF-8):Narzędzie linii poleceń
Name:		rl
Version:	0.2.6
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://ch.tudelft.nl/~arthur/rl/%{name}-%{version}.tar.gz
# Source0-md5:	5505b1ff129ac95fa2a27ee4073d81e4
URL:		http://ch.tudelft.nl/~arthur/rl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rl is a command-line tool that reads lines from an input file or
stdin, randomizes the lines and outputs a specified number of lines.

%description -l pl.UTF-8
rl jest narzędziem linii poleceń, które czyta linijki z pliku lub
standardowego wejścia i wypisuje określoną ich ilość w losowej
kolejności.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
